# import fastapi router
from fastapi import APIRouter
# import model classes
from ml.models_classes import CategoryClassifier, PriorityClassifier
# import category encoder to encode the category string
from ml.category_encoder import CategoryEncoder
# import cleaning function to clean the raw text
from utils.data_cleaning import clean_text
# import global settings class
from config import Settings
# import hstack from scipy.sparse to combine sparse matrices
from scipy.sparse import hstack

config = Settings()

# Load the model paths from the config
category_classifier_model_path = config.category_classifier_model_path
category_classifier_vectorizer_path = config.category_classifier_vectorizer_path

priority_classifier_model_path = config.priority_classifier_model_path
priority_classifier_vectorizer_path = config.priority_classifier_vectorizer_path

# Initialize the classifiers and encoder
category_classifier = CategoryClassifier(
    path_to_model=category_classifier_model_path,
    path_to_vectorizer=category_classifier_vectorizer_path,
)

priority_classifier = PriorityClassifier(
    path_to_model=priority_classifier_model_path,
    path_to_vectorizer=priority_classifier_vectorizer_path,
)

category_encoder = CategoryEncoder(
    path_to_encoder=config.category_encoder_path,
)

# Create a FastAPI router
router = APIRouter()

# Prediction endpoint
@router.post("/predict")
def get_predictions(text: str):
    """
    Predict the category and priority of the given text.
    Args:
        text (str): The input text to classify.
    Returns:
        dict: A dictionary containing the predicted category and priority.
    """
    # Clean the text
    preprocessed_text = clean_text(text)
    
    # Predict the category
    category = category_classifier.predict(preprocessed_text)
    
    # Combine the vectorized text and encoded category
    # into a single sparse matrix for the priority classifier
    combined_feature = hstack([
        priority_classifier.vectorize(preprocessed_text),
        category_encoder.encode(category),
    ])
    
    # Predict the priority
    priority = priority_classifier.predict(combined_feature)
    
    # Print the predictions for debugging purposes
    print(f"Predicted category: {category}")
    print(f"Predicted priority: {priority}")
    
    # Return the results
    result = {
        "category": category,
        "priority": priority,
    }
    return result