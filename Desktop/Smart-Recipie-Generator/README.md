# Smart Recipe Generator

A beautiful, AI-powered web application that suggests recipes based on available ingredients. Built with Flask and modern web technologies.

## Features

- **Image Recognition**: Upload photos of ingredients for automatic detection
- **Smart Recipe Matching**: Advanced algorithm finds perfect recipes for your ingredients
- **Dietary Preferences**: Filter by vegetarian, gluten-free, vegan, and more
- **Mobile Responsive**: Works perfectly on all devices
- **Favorite Recipes**: Save your favorite recipes for quick access
- **Nutrition Information**: Detailed nutrition facts for each recipe
- **Beautiful UI**: Modern, colorful design with smooth animations

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with CSS Grid and Flexbox
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Poppins)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd smart-recipe-generator
2. **Create virtual env**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt

4. **Run the application**
    ```bash
    python app.py

## Project Structure

smart-recipe-generator/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
│
├── static/              # Static files
│   ├── css/            # Stylesheets
│   ├── js/             # JavaScript files
│   ├── images/         # Recipe images and icons
│   └── uploads/        # User uploaded images
│
├── templates/           # HTML templates
│   ├── base.html       # Base template
│   ├── index.html      # Home page
│   ├── upload.html     # Ingredient input page
│   ├── recipes.html    # Recipe results page
│   ├── recipe-detail.html # Individual recipe page
│   └── favorites.html  # Favorite recipes page
│
├── models/             # Business logic
│   ├── recipe_generator.py
│   └── image_processor.py
│
├── utils/              # Utility functions
│   ├── helpers.py
│   └── validators.py
│
└── data/               # Recipe data
    └── recipes.json


## API Integration

The application can integrate with:

Spoonacular API (150 free requests/day)

Edamam Recipe API (10,000 free requests/month)

Clarifai Food Recognition (1,000 free operations/month)

Note: The application works completely offline with sample data if no API keys are provided.