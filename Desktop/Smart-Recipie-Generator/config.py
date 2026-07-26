import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-123-smart-recipe'
    UPLOAD_FOLDER = 'static/uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    
    # Spoonacular API (Free tier: 150 requests per day)
    SPOONACULAR_API_KEY = os.environ.get('SPOONACULAR_API_KEY') or 'demo_key'
    
    # Edamam API (Free tier: 10,000 requests per month)
    EDAMAM_APP_ID = os.environ.get('EDAMAM_APP_ID') or 'demo_id'
    EDAMAM_APP_KEY = os.environ.get('EDAMAM_APP_KEY') or 'demo_key'