# import fastapi router
from fastapi import APIRouter
# import model classes
from app.ml.models_classes import CategoryClassifier, PriorityClassifier
# import category encoder to encode the category string
from app.ml.category_encoder import CategoryEncoder
# import cleaning function to clean the raw text
from app.utils.data_cleaning import clean_text
# import logger to log the predictions
from app.utils.logger import get_logger
# import global settings class
from app.config import Settings
# import hstack from scipy.sparse to combine sparse matrices
from scipy.sparse import hstack
# import input and prediction output schemas
from app.utils.schemas import PredictionInputSchema, PredictionOutputSchema
# import time for calculating the prediction time
import time

logger = get_logger(__name__)

# Load the model paths from the config
category_classifier_model_path = Settings.CATEGORY_CLASSIFIER_MODEL_PATH
category_classifier_vectorizer_path = Settings.CATEGORY_CLASSIFIER_VECTORIZER_PATH

priority_classifier_model_path = Settings.PRIORITY_CLASSIFIER_MODEL_PATH
priority_classifier_vectorizer_path = Settings.PRIORITY_CLASSIFIER_VECTORIZER_PATH

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
    path_to_encoder=Settings.CATEGORY_ENCODER_PATH,
)

# Create a FastAPI router
router = APIRouter()

# Prediction endpoint
@router.post("/predict")
def get_predictions(payload: PredictionInputSchema):
    """
    Predict the category and priority of the given text.
    Args:
        text (str): The input text to classify.
    Returns:
        dict: A dictionary containing the predicted category and priority.
    """
    # start the timer to measure the time taken for prediction
    start_time = time.time()
    # Extract the text from the payload
    raw_text = payload.text
    
    # Clean the text
    preprocessed_text = clean_text(raw_text)
    
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
    
    time_taken_before_logging = time.time() - start_time
    # Log
    logger.info(f"Text: {raw_text}, Category: {category}, Priority: {priority}, Time taken: {time_taken_before_logging:.2f} seconds")
    
    total_time = time.time() - start_time
    # Return the results
    return PredictionOutputSchema(
        category=category,
        priority=priority,
        response_time=total_time,
    )