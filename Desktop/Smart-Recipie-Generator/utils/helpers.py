import os
import json
from datetime import datetime
from flask import session

def save_uploaded_file(file, upload_folder):
    """Save uploaded file and return file path"""
    if file and file.filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}_{file.filename}"
        filepath = os.path.join(upload_folder, filename)
        file.save(filepath)
        return filename
    return None

def load_recipes_from_json(filepath='data/recipes.json'):
    """Load recipes from JSON file"""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def calculate_match_score(recipe_ingredients, user_ingredients):
    """Calculate match score between recipe and user ingredients"""
    score = 0
    recipe_ingredients_lower = [ing.lower() for ing in recipe_ingredients]
    user_ingredients_lower = [ing.lower() for ing in user_ingredients]
    
    for user_ing in user_ingredients_lower:
        for recipe_ing in recipe_ingredients_lower:
            if user_ing in recipe_ing or recipe_ing in user_ing:
                score += 2  # Exact match
            elif any(word in recipe_ing for word in user_ing.split()) or any(word in user_ing for word in recipe_ing.split()):
                score += 1  # Partial match
    
    return score

def filter_recipes_by_diet(recipes, diet):
    """Filter recipes by dietary preference"""
    if not diet:
        return recipes
    
    return [recipe for recipe in recipes if diet in recipe.get('diets', [])]

def filter_recipes_by_time(recipes, max_time):
    """Filter recipes by maximum cooking time"""
    if not max_time:
        return recipes
    
    max_time = int(max_time)
    return [recipe for recipe in recipes if recipe.get('readyInMinutes', 0) <= max_time]

def get_user_favorites():
    """Get user's favorite recipes from session"""
    return session.get('favorites', [])

def add_to_favorites(recipe_id):
    """Add recipe to user's favorites"""
    favorites = get_user_favorites()
    if recipe_id not in favorites:
        favorites.append(recipe_id)
        session['favorites'] = favorites
        return True
    return False

def remove_from_favorites(recipe_id):
    """Remove recipe from user's favorites"""
    favorites = get_user_favorites()
    if recipe_id in favorites:
        favorites.remove(recipe_id)
        session['favorites'] = favorites
        return True
    return False

def format_nutrition_info(nutrition_data):
    """Format nutrition information for display"""
    if not nutrition_data:
        return {
            'calories': 0,
            'protein': 0,
            'carbs': 0,
            'fat': 0
        }
    
    return {
        'calories': nutrition_data.get('calories', 0),
        'protein': nutrition_data.get('protein', 0),
        'carbs': nutrition_data.get('carbs', 0),
        'fat': nutrition_data.get('fat', 0)
    }