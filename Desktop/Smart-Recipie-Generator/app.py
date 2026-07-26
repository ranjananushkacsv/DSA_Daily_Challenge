from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
import os
import json
from werkzeug.utils import secure_filename
from config import Config
from models.recipe_generator import RecipeGenerator
from models.image_processor import ImageProcessor

app = Flask(__name__)
app.config.from_object(Config)

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize components
recipe_gen = RecipeGenerator()
image_processor = ImageProcessor()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_ingredients():
    if request.method == 'POST':
        # Handle image upload
        if 'image' in request.files:
            image_file = request.files['image']
            if image_file and image_file.filename != '' and allowed_file(image_file.filename):
                filename = secure_filename(image_file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                image_file.save(filepath)
                
                # Process image to get ingredients
                ingredients = image_processor.process_image(filepath)
                session['ingredients'] = ingredients
                session['uploaded_image'] = filename
                flash('Ingredients detected from image!', 'success')
                # REDIRECT instead of render_template
                return redirect(url_for('upload_ingredients'))
        
        # Handle manual ingredient input
        ingredients_text = request.form.get('ingredients', '')
        if ingredients_text:
            ingredients = [ing.strip() for ing in ingredients_text.split(',') if ing.strip()]
            session['ingredients'] = ingredients
            session.pop('uploaded_image', None)
            flash('Ingredients added successfully!', 'success')
            # REDIRECT instead of render_template
            return redirect(url_for('upload_ingredients'))
    
    # GET request - display current ingredients and image
    ingredients = session.get('ingredients', [])
    image_url = None
    if 'uploaded_image' in session:
        image_url = url_for('static', filename=f'uploads/{session["uploaded_image"]}')
    
    return render_template('upload.html', 
                         ingredients=ingredients, 
                         image_url=image_url)

@app.route('/recipes')
def get_recipes():
    ingredients = session.get('ingredients', [])
    if not ingredients:
        flash('Please add some ingredients first!', 'warning')
        return redirect(url_for('upload_ingredients'))
    
    # Get filters
    dietary_prefs = request.args.get('diet', '')
    max_time = request.args.get('max_time', '')
    cuisine = request.args.get('cuisine', '')
    
    recipes = recipe_gen.get_recipes(ingredients, dietary_prefs, max_time, cuisine)
    return render_template('recipes.html', 
                         recipes=recipes, 
                         ingredients=ingredients,
                         diet=dietary_prefs,
                         max_time=max_time)

@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    recipe = recipe_gen.get_recipe_details(recipe_id)
    if not recipe:
        flash('Recipe not found!', 'error')
        return redirect(url_for('get_recipes'))
    return render_template('recipe-detail.html', recipe=recipe)

@app.route('/favorites')
def favorites():
    favorites = session.get('favorites', [])
    favorite_recipes = []
    for recipe_id in favorites:
        recipe = recipe_gen.get_recipe_details(recipe_id)
        if recipe:
            favorite_recipes.append(recipe)
    return render_template('favorites.html', favorites=favorite_recipes)

@app.route('/toggle_favorite/<int:recipe_id>', methods=['POST'])
def toggle_favorite(recipe_id):
    if 'favorites' not in session:
        session['favorites'] = []
    
    favorites = session['favorites']
    if recipe_id in favorites:
        favorites.remove(recipe_id)
        message = 'Recipe removed from favorites'
    else:
        favorites.append(recipe_id)
        message = 'Recipe added to favorites!'
    
    session['favorites'] = favorites
    return jsonify({'success': True, 'message': message, 'is_favorite': recipe_id in favorites})

@app.route('/clear_ingredients')
def clear_ingredients():
    session.pop('ingredients', None)
    session.pop('uploaded_image', None)
    flash('Ingredients cleared!', 'info')
    return redirect(url_for('upload_ingredients'))

if __name__ == '__main__':
    app.run(debug=True)