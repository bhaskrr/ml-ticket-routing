from huggingface_hub import hf_hub_download
import joblib
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def load_model(model_name: str, save_to: str):
    model_path = hf_hub_download(
        repo_id=os.environ.get("REPO_ID"),
        filename=model_name,
        repo_type="model",
    )
    model = joblib.load(model_path)
    joblib.dump(model, save_to)