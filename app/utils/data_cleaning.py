import spacy
nlp = spacy.load("en_core_web_sm")

# Function to clean the text data
def clean_text(sentence):
    doc = nlp(sentence)
    sentence = sentence.strip() # Remove leading and trailing whitespace
    sentence = sentence.replace(r"\s+", " ") # Replace multiple spaces with a single space
    sentence = " ".join(str(token) for token in doc if token.is_alpha) # Remove non-alphanumeric characters
    return sentence