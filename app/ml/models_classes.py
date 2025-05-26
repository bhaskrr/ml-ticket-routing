import joblib
import os
from app.utils.load_models import load_model

class CategoryClassifier:
    def __init__(self, path_to_model: str, path_to_vectorizer: str):
        # Load model
        load_model(path_to_model.split("/")[-1], save_to=path_to_model)
        
        if not os.path.exists(path_to_model):
            raise FileNotFoundError(f"Model file not found: {path_to_model}")
        if not os.path.exists(path_to_vectorizer):
            raise FileNotFoundError(f"Vectorizer file not found: {path_to_vectorizer}")
        self.path = path_to_model
        self.model = joblib.load(self.path)
        self.vectorizer = joblib.load(path_to_vectorizer)
    
    def predict(self, text: str):
        """
        Predict the category of a given text.
        Args:
            text (str): The text to classify.
        Returns:
            str: The predicted category.
        """
        vectors = self.vectorizer.transform([text])
        prediction = self.model.predict(vectors)
        return prediction[0]

class PriorityClassifier:
    def __init__(self, path_to_model: str, path_to_vectorizer: str):
        # Load model
        load_model(model_name= path_to_model.split("/")[-1], save_to= path_to_model)
        
        if not os.path.exists(path_to_model):
            raise FileNotFoundError(f"Model file not found: {path_to_model}")
        if not os.path.exists(path_to_vectorizer):
            raise FileNotFoundError(f"Vectorizer file not found: {path_to_vectorizer}")
        self.path = path_to_model
        self.model = joblib.load(self.path)
        self.classes = self.model.classes_
        self.vectorizer = joblib.load(path_to_vectorizer)
    
    def vectorize(self, text: str):
        """
        Vectorize the input text.
        Args:
            text (str): The text to vectorize.
        Returns:
            sparse matrix: The vectorized text.
        """
        return self.vectorizer.transform([text])
    
    def predict(self, vectors):
        """
        Predict the priority of a given vectorized text.
        Args:
            vectors (sparse matrix): The vectorized text.
        Returns:
            str: The predicted priority.
        """
        prediction = self.model.predict(vectors)
        return prediction[0]