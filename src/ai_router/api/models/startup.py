# Initializes Pythonic Model Classes from ./models.json  / ON STARTUP
import json

from .ai_model import AIModel

def read_models(file_path: str):
  dicted_models = {}
    
  with open(file_path, 'r') as f: 
    dicted_models = json.loads(f.read())
    
  return dicted_models.get('ai_models', {})

DEFAULT_AI_MODELS_FILE_PATH = r'C:\Users\furka\Desktop\ai-router\ai-router\src\ai_router\api\models\ai_models.json'

def initalize_models(file_path: str = DEFAULT_AI_MODELS_FILE_PATH):

  """Initializes models from a JSON file."""
  dicted_models = read_models(file_path)
  
  for model in dicted_models:
    model_name = model.get('name')
    model_version = model.get('version')
    model_description = model.get('description', "")
    model_endpoint = model.get('endpoint', "")
    model_token = model.get('token', "")
    
    # Create a Model instance
    model_instance = AIModel(name=model_name, version=model_version, description=model_description, endpoint=model_endpoint, token=model_token)
    
    print(f"Initialized model: {model_instance}")
    
  print("All models have been initialized.")