import re

def validate_ingredients(ingredients_list):
    """Validate and clean ingredients list"""
    if not ingredients_list:
        return []
    
    # Remove empty strings and strip whitespace
    cleaned = [ing.strip() for ing in ingredients_list if ing.strip()]
    
    # Remove duplicates while preserving order
    seen = set()
    unique_ingredients = []
    for ing in cleaned:
        if ing.lower() not in seen:
            seen.add(ing.lower())
            unique_ingredients.append(ing)
    
    return unique_ingredients

def validate_dietary_preference(diet):
    """Validate dietary preference input"""
    valid_diets = ['vegetarian', 'vegan', 'gluten free', 'dairy free', '']
    return diet if diet in valid_diets else ''

def validate_cooking_time(max_time):
    """Validate cooking time input"""
    try:
        if not max_time:
            return ''
        time = int(max_time)
        return str(time) if time > 0 else ''
    except (ValueError, TypeError):
        return ''

def validate_servings(servings):
    """Validate servings input"""
    try:
        if not servings:
            return 1
        servings = int(servings)
        return max(1, min(servings, 20))  # Limit to 20 servings
    except (ValueError, TypeError):
        return 1

def sanitize_filename(filename):
    """Sanitize filename for safe storage"""
    if not filename:
        return None
    
    # Remove path components and special characters
    filename = re.sub(r'[^a-zA-Z0-9._-]', '_', filename)
    return filename

def validate_image_file(filename, allowed_extensions=None):
    """Validate image file extension"""
    if allowed_extensions is None:
        allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    
    if not filename:
        return False
    
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions