import random
from app.config import Settings, CATEGORY_LABELS
from app.ml.category_encoder import CategoryEncoder

def test_category_encoder():
    """Test the CategoryEncoder class."""
    
    # Initialize the encoder
    encoder = CategoryEncoder(
        path_to_encoder=Settings.CATEGORY_ENCODER_PATH,
    )
    
    # Randomly select a category label from the predefined labels
    index = random.randint(0, len(CATEGORY_LABELS) - 1)
    
    # Encode a random category label
    category_label = CATEGORY_LABELS[index]
    encoded_category = encoder.encode(category_label)
    
    # Check if the encoded category is a sparse matrix
    assert hasattr(encoded_category, "shape"), "Encoding did not return a sparse matrix."