from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_prediction_valid_input():
    """Test the prediction endpoint with a valid input text."""
    text = """Dear Customer Support Team,\n\nI am writing to report a significant problem with the
    centralized account management portal, which currently appears to be offline. This outage is
    blocking access to account settings, leading to substantial inconvenience. I have attempted
    to log in multiple times using different browsers and devices, but the issue persists.\n\n
    Could you please provide an update on the outage status and an estimated time for resolution?
    Also, are there any alternative ways to access and manage my account during this downtime?"""
    
    response = client.post("/api/v1/predict", json={"text": text})
    assert response.status_code == 200
    data = response.json()
    assert "category" in data
    assert "priority" in data

def test_prediction_invalid_input_field():
    """Test the prediction endpoint with an invalid input field."""
    response = client.post("/api/v1/predict", json={"wrong_field": "oops"})
    assert response.status_code == 422
    response_data = response.json()
    assert "detail" in response_data
    assert "body" in response_data

def test_prediction_empty_text():
    """Test the prediction endpoint with an empty text input."""
    response = client.post("/api/v1/predict", json={"text": ""})
    assert response.status_code == 422
    response_data = response.json()
    assert "detail" in response_data
    assert "body" in response_data

def test_prediction_missing_text():
    """Test the prediction endpoint with a missing text field."""
    response = client.post("/api/v1/predict", json={})
    assert response.status_code == 422
    response_data = response.json()
    assert "detail" in response_data
    assert "body" in response_data

def test_prediction_non_text_input():
    """Test the prediction endpoint with a non-text input."""
    response = client.post("/api/v1/predict", json={"text": 12345})
    assert response.status_code == 422
    response_data = response.json()
    assert "detail" in response_data
    assert "body" in response_data

def test_prediction_list_input():
    """Test the prediction endpoint with a list input instead of a string"""
    response = client.post("/api/v1/predict", json={"text": ["This is a list", "of strings"]})
    assert response.status_code == 422
    response_data = response.json()
    assert "detail" in response_data
    assert "body" in response_data

def test_prediction_special_characters():
    """Test the prediction endpoint with special characters in the text."""
    text = "Hello, @there. This is a test! #SpecialCharacters $%^&*()"
    response = client.post("/api/v1/predict", json={"text": text})
    assert response.status_code == 200
    data = response.json()
    assert "category" in data
    assert "priority" in data

def test_prediction_malformed_json():
    """Test the prediction endpoint with malformed JSON input."""
    response = client.post("/api/v1/predict", content='{"text": "This is a test. This is a malformed JSON"}')
    assert response.status_code == 200
    data = response.json()
    assert "category" in data
    assert "priority" in data

def test_prediction_large_text():
    """Test the prediction endpoint with a very large text input."""
    large_text = "A" * 2000 # Larger than input size limit
    response = client.post("/api/v1/predict", json={"text": large_text})
    assert response.status_code == 422
    response_data = response.json()
    assert "detail" in response_data
    assert "body" in response_data

def test_prediction_latency():
    """Test the prediction endpoint for response time."""
    text = "A" * 1000 # Max input size
    response = client.post("/api/v1/predict", json={"text": text})
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2 # Check if response time is under 2 seconds