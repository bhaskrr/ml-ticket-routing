import os

class Settings:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    category_classifier_model_path: str = os.path.join(base_dir, "ml/models/category_classifier.joblib")
    category_classifier_vectorizer_path: str = os.path.join(base_dir, "ml/vectorizers/category_classifier/vectorizer.joblib")
    priority_classifier_model_path: str = os.path.join(base_dir, "ml/models/priority_classifier.joblib")
    priority_classifier_vectorizer_path: str = os.path.join(base_dir, "ml/vectorizers/priority_classifier/vectorizer.joblib")
    category_encoder_path: str = os.path.join(base_dir, "ml/encoders/category_encoder.joblib")