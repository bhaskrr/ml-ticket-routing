from app.ml.models_classes import CategoryClassifier, PriorityClassifier
from app.config import Settings, CATEGORY_LABELS, PRIORITY_LABELS
from app.ml.category_encoder import CategoryEncoder
from scipy.sparse import hstack
import random

def test_category_classifier():
    """Test the CategoryClassifier class."""
    
    # Initialize the classifier with paths to model and vectorizer
    classifier = CategoryClassifier(
        path_to_model=Settings.CATEGORY_CLASSIFIER_MODEL_PATH,
        path_to_vectorizer=Settings.CATEGORY_CLASSIFIER_VECTORIZER_PATH,
    )
    
    # Test prediction with a sample text
    sample_text = "This is a test text for category classification."
    prediction = classifier.predict(sample_text)
    
    # Check if the prediction is a string (category)
    assert isinstance(prediction, str)
    
    # Check if the predicted category is in the predefined labels
    assert prediction in CATEGORY_LABELS, f"Predicted category '{prediction}' is not in predefined labels."

def test_priority_classifier():
    """Test the PriorityClassifier class."""
    
    # Initialize the classifier with paths to model and vectorizer
    classifier = PriorityClassifier(
        path_to_model=Settings.PRIORITY_CLASSIFIER_MODEL_PATH,
        path_to_vectorizer=Settings.PRIORITY_CLASSIFIER_VECTORIZER_PATH,
    )
    
    # Initialize the category encoder
    category_encoder = CategoryEncoder(
        path_to_encoder=Settings.CATEGORY_ENCODER_PATH,
    )
    
    # Test vectorization with a sample text
    sample_text = "This is a test text for priority classification."
    vectors = classifier.vectorize(sample_text)
    
    # Check if the output is a sparse matrix
    assert hasattr(vectors, 'shape'), "Vectorization did not return a sparse matrix."
    
    # Randomly select a category label from the predefined labels
    index = random.randint(0, len(CATEGORY_LABELS) - 1)
    
    # Encode a random category label
    category_label = CATEGORY_LABELS[index]
    encoded_category = category_encoder.encode(category_label)
    
    # Combine the vectorized text and encoded category
    combined_feature = hstack([vectors, encoded_category])
    
    # Test prediction with the vectorized text
    prediction = classifier.predict(combined_feature)
    
    # Check if the prediction is a string (priority)
    assert isinstance(prediction, str)
    
    # Check if the predicted priority is in the predefined labels
    assert prediction in PRIORITY_LABELS, f"Predicted priority '{prediction}' is not in predefined labels."