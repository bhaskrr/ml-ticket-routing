import joblib
import numpy as np

class CategoryEncoder:
    def __init__(self, path_to_encoder: str):
        self.path = path_to_encoder
        self.encoder = joblib.load(self.path)
    
    def encode(self, text: str):
        """
        Encode the input text.
        Args:
            text (str): The text to encode.
        Returns:
            int: The encoded category.
        """
        return self.encoder.transform(np.array(text).reshape(1, -1))