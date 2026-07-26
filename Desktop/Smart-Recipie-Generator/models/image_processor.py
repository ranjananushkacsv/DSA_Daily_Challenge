import random

class ImageProcessor:
    def __init__(self):
        self.common_ingredients = [
            'apple', 'banana', 'orange', 'strawberry', 'blueberry', 'raspberry',
            'carrot', 'broccoli', 'spinach', 'tomato', 'potato', 'sweet potato',
            'onion', 'garlic', 'bell pepper', 'cucumber', 'lettuce', 'kale',
            'chicken breast', 'ground beef', 'salmon', 'shrimp', 'egg', 'milk',
            'cheese', 'yogurt', 'butter', 'flour', 'sugar', 'honey',
            'rice', 'pasta', 'bread', 'avocado', 'mushroom', 'zucchini',
            'lemon', 'lime', 'cilantro', 'basil', 'parsley', 'thyme'
        ]
    
    def process_image(self, image_path):
        """
        Simulate image processing - returns realistic ingredient combinations
        No API needed - completely free
        """
        import time
        time.sleep(1.5)  # Simulate processing time
        
        # Create realistic ingredient combinations
        food_groups = {
            'breakfast': ['egg', 'milk', 'bread', 'butter', 'cheese', 'yogurt', 'banana', 'strawberry'],
            'salad': ['lettuce', 'tomato', 'cucumber', 'onion', 'carrot', 'bell pepper', 'lemon', 'olive oil'],
            'smoothie': ['banana', 'strawberry', 'blueberry', 'yogurt', 'milk', 'honey'],
            'stir_fry': ['bell pepper', 'carrot', 'broccoli', 'onion', 'garlic', 'chicken breast', 'soy sauce'],
            'pasta': ['pasta', 'tomato', 'garlic', 'onion', 'basil', 'cheese'],
            'soup': ['potato', 'carrot', 'onion', 'celery', 'garlic', 'vegetable broth']
        }
        
        # Detect based on common patterns (simulated)
        detected_ingredients = []
        
        # Always include 1-2 very common ingredients
        detected_ingredients.extend(random.sample(
            ['onion', 'garlic', 'salt', 'pepper', 'olive oil', 'butter'], 
            random.randint(1, 2)
        ))
        
        # Add 2-3 main ingredients
        main_ingredients = random.sample(self.common_ingredients, random.randint(2, 3))
        detected_ingredients.extend(main_ingredients)
        
        return list(set(detected_ingredients))  # Remove duplicates