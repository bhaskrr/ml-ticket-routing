import os

class Settings:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    CATEGORY_CLASSIFIER_MODEL_PATH: str = os.path.join(BASE_DIR, "ml/models/category_classifier.joblib")
    CATEGORY_CLASSIFIER_VECTORIZER_PATH: str = os.path.join(BASE_DIR, "ml/vectorizers/category_classifier/vectorizer.joblib")
    PRIORITY_CLASSIFIER_MODEL_PATH: str = os.path.join(BASE_DIR, "ml/models/priority_classifier.joblib")
    PRIORITY_CLASSIFIER_VECTORIZER_PATH: str = os.path.join(BASE_DIR, "ml/vectorizers/priority_classifier/vectorizer.joblib")
    CATEGORY_ENCODER_PATH: str = os.path.join(BASE_DIR, "ml/encoders/category_encoder.joblib")

CATEGORY_LABELS = [
    "Technical Support",
    "Product Support",
    "Customer Service",
    "IT Support",
    "Billing and Payments",
    "Returns and Exchanges",
    "Service Outages and Maintenance",
    "Sales and Pre-Sales",
    "Human Resources",
    "General Inquiry",
]

PRIORITY_LABELS = [
    "Low",
    "Medium",
    "High",
]