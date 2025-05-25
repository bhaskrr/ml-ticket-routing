from app.utils.data_cleaning import clean_text

def test_clean_text():
    """Test the clean_text function with various inputs."""
    # Test with a simple sentence
    assert clean_text("Hello, world!") == "Hello world"
    
    # Test with leading and trailing whitespaces
    assert clean_text("  Hello, world!  ") == "Hello world"
    
    # Test with multiple spaces
    assert clean_text("Hello,   world!") == "Hello world"
    
    # Test with special characters
    assert clean_text("Hello, @world! #test") == "Hello test"
    
    # Test with an empty string
    assert clean_text("") == ""
    
    # Test with only non-alphanumeric characters
    assert clean_text("!!!") == ""
    
    # Test with a sentence containing numbers
    assert clean_text("Hello 123, world!") == "Hello world"