import google.generativeai as genai
import os

# Configure the Generative AI API
GOOGLE_API_KEY = ""
genai.configure(api_key=GOOGLE_API_KEY)

# List available models
def list_models():
    try:
        models = genai.list_models()
        print("Available Models:")
        for model in models:
            print(model)
    except Exception as e:
        print(f"Error listing models: {e}")

# Call list_models to check available models
list_models()
