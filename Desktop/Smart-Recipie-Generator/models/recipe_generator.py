import requests
import json
import random
from config import Config

class RecipeGenerator:
    def __init__(self):
        self.api_key = Config.SPOONACULAR_API_KEY
        self.base_url = "https://api.spoonacular.com"
        self.recipes = self._load_sample_recipes()
    
    def _load_sample_recipes(self):
        """Load comprehensive sample recipes"""
        try:
            with open('data/recipes.json', 'r') as f:
                return json.load(f)
        except:
            return self._get_default_recipes()
    
    def _get_default_recipes(self):
        """Comprehensive default recipes - no API needed"""
        return [
            {
                'id': 1,
                'title': 'Vegetable Stir Fry',
                'image': '/static/images/recipe1.jpg',
                'readyInMinutes': 20,
                'servings': 2,
                'diets': ['vegetarian', 'gluten free'],
                'ingredients': ['bell pepper', 'carrot', 'broccoli', 'soy sauce', 'garlic', 'onion'],
                'instructions': '1. Chop all vegetables into bite-sized pieces\n2. Heat oil in a wok or large pan\n3. Stir-fry garlic and onions until fragrant\n4. Add harder vegetables first (carrots, broccoli)\n5. Add remaining vegetables and stir-fry for 5-7 minutes\n6. Add soy sauce and serve hot',
                'nutrition': {'calories': 250, 'protein': 8, 'carbs': 35, 'fat': 10},
                'cuisine': 'Asian',
                'difficulty': 'Easy'
            },
            {
                'id': 2,
                'title': 'Fruit Smoothie Bowl',
                'image': '/static/images/recipe2.jpg', 
                'readyInMinutes': 5,
                'servings': 1,
                'diets': ['vegetarian', 'gluten free', 'dairy free'],
                'ingredients': ['banana', 'strawberry', 'blueberry', 'yogurt', 'honey', 'granola'],
                'instructions': '1. Blend banana, strawberries, and yogurt until smooth\n2. Pour into a bowl\n3. Top with blueberries, granola, and drizzle with honey',
                'nutrition': {'calories': 180, 'protein': 5, 'carbs': 40, 'fat': 2},
                'cuisine': 'International',
                'difficulty': 'Very Easy'
            },
            {
                'id': 3,
                'title': 'Classic Omelette',
                'image': '/static/images/recipe3.jpg',
                'readyInMinutes': 10,
                'servings': 1,
                'diets': ['vegetarian', 'gluten free'],
                'ingredients': ['egg', 'cheese', 'milk', 'butter', 'salt', 'pepper'],
                'instructions': '1. Beat eggs with milk, salt, and pepper\n2. Melt butter in a non-stick pan\n3. Pour egg mixture and cook until edges set\n4. Add cheese and fold omelette in half\n5. Cook for another minute and serve',
                'nutrition': {'calories': 320, 'protein': 22, 'carbs': 2, 'fat': 25},
                'cuisine': 'French',
                'difficulty': 'Easy'
            },
            {
                'id': 4,
                'title': 'Pasta with Tomato Sauce',
                'image': '/static/images/recipe4.jpg',
                'readyInMinutes': 25,
                'servings': 2,
                'diets': ['vegetarian'],
                'ingredients': ['pasta', 'tomato', 'garlic', 'onion', 'basil', 'olive oil'],
                'instructions': '1. Cook pasta according to package directions\n2. Sauté garlic and onions in olive oil\n3. Add chopped tomatoes and cook until soft\n4. Blend sauce until smooth, add basil\n5. Mix sauce with pasta and serve',
                'nutrition': {'calories': 400, 'protein': 12, 'carbs': 75, 'fat': 8},
                'cuisine': 'Italian',
                'difficulty': 'Easy'
            },
            {
                'id': 5,
                'title': 'Chicken Salad',
                'image': '/static/images/recipe5.jpg',
                'readyInMinutes': 15,
                'servings': 2,
                'diets': ['gluten free'],
                'ingredients': ['chicken', 'lettuce', 'tomato', 'cucumber', 'olive oil', 'lemon'],
                'instructions': '1. Cook and shred chicken breast\n2. Chop all vegetables\n3. Mix chicken with vegetables\n4. Dress with olive oil and lemon juice\n5. Season with salt and pepper',
                'nutrition': {'calories': 280, 'protein': 25, 'carbs': 10, 'fat': 15},
                'cuisine': 'American',
                'difficulty': 'Easy'
            },
            {
                'id': 6,
                'title': 'Avocado Toast',
                'image': '/static/images/recipe6.jpg',
                'readyInMinutes': 5,
                'servings': 1,
                'diets': ['vegetarian', 'gluten free'],
                'ingredients': ['avocado', 'bread', 'lemon', 'salt', 'pepper', 'chili flakes'],
                'instructions': '1. Toast bread until golden\n2. Mash avocado with lemon juice, salt, and pepper\n3. Spread avocado mixture on toast\n4. Sprinkle with chili flakes and serve',
                'nutrition': {'calories': 220, 'protein': 5, 'carbs': 25, 'fat': 12},
                'cuisine': 'International',
                'difficulty': 'Very Easy'
            },
            {
                'id': 7,
                'title': 'Vegetable Soup',
                'image': '/static/images/recipe7.jpg',
                'readyInMinutes': 30,
                'servings': 4,
                'diets': ['vegetarian', 'gluten free', 'vegan'],
                'ingredients': ['carrot', 'potato', 'onion', 'celery', 'vegetable broth', 'herbs'],
                'instructions': '1. Chop all vegetables\n2. Sauté onions and celery until soft\n3. Add remaining vegetables and broth\n4. Simmer for 20 minutes until vegetables are tender\n5. Season with herbs and serve hot',
                'nutrition': {'calories': 120, 'protein': 4, 'carbs': 25, 'fat': 1},
                'cuisine': 'International',
                'difficulty': 'Easy'
            },
            {
                'id': 8,
                'title': 'Berry Parfait',
                'image': '/static/images/recipe8.jpg',
                'readyInMinutes': 5,
                'servings': 1,
                'diets': ['vegetarian', 'gluten free'],
                'ingredients': ['yogurt', 'strawberry', 'blueberry', 'granola', 'honey'],
                'instructions': '1. Layer yogurt at the bottom of a glass\n2. Add a layer of mixed berries\n3. Sprinkle with granola\n4. Repeat layers and top with honey',
                'nutrition': {'calories': 200, 'protein': 8, 'carbs': 35, 'fat': 4},
                'cuisine': 'International',
                'difficulty': 'Very Easy'
            }
        ]
    
    def get_recipes(self, ingredients, diet='', max_time='', cuisine=''):
        """Get recipes - works completely offline with sample data"""
        # Use sample data directly - no API calls needed
        return self._get_matching_sample_recipes(ingredients, diet, max_time, cuisine)
    
    def get_recipe_details(self, recipe_id):
        """Get detailed recipe - works offline"""
        for recipe in self.recipes:
            if recipe['id'] == recipe_id:
                return recipe
        return None
    
    def _get_matching_sample_recipes(self, ingredients, diet, max_time, cuisine):
        """Smart recipe matching with sample data"""
        matching_recipes = []
        ingredients_lower = [ing.lower() for ing in ingredients]
        
        for recipe in self.recipes:
            # Calculate match score based on ingredients
            match_score = self._calculate_match_score(recipe, ingredients_lower)
            
            if match_score > 0:  # At least one ingredient matches
                # Apply filters
                if diet and diet not in recipe.get('diets', []):
                    continue
                if max_time and recipe.get('readyInMinutes', 0) > int(max_time):
                    continue
                if cuisine and cuisine.lower() not in recipe.get('cuisine', '').lower():
                    continue
                
                # Determine used and missed ingredients
                used_ingredients = []
                missed_ingredients = []
                
                for recipe_ing in recipe.get('ingredients', []):
                    recipe_ing_lower = recipe_ing.lower()
                    if any(user_ing in recipe_ing_lower for user_ing in ingredients_lower):
                        used_ingredients.append(recipe_ing)
                    else:
                        missed_ingredients.append(recipe_ing)
                
                matching_recipes.append({
                    'id': recipe['id'],
                    'title': recipe['title'],
                    'image': recipe.get('image', ''),
                    'usedIngredients': used_ingredients,
                    'missedIngredients': missed_ingredients,
                    'matchScore': match_score,
                    'readyInMinutes': recipe.get('readyInMinutes', 0),
                    'likes': random.randint(50, 200)
                })
        
        # Sort by match score (highest first)
        matching_recipes.sort(key=lambda x: x['matchScore'], reverse=True)
        return matching_recipes[:12]
    
    def _calculate_match_score(self, recipe, user_ingredients_lower):
        """Calculate how well the recipe matches user ingredients"""
        score = 0
        recipe_ingredients_lower = [ing.lower() for ing in recipe.get('ingredients', [])]
        
        for user_ing in user_ingredients_lower:
            for recipe_ing in recipe_ingredients_lower:
                if user_ing in recipe_ing or recipe_ing in user_ing:
                    score += 2  # Exact match
                elif any(word in recipe_ing for word in user_ing.split()) or any(word in user_ing for word in recipe_ing.split()):
                    score += 1  # Partial match
        
        return score