"""
This is the file for the recipe routes
"""
from flask import Blueprint, request, jsonify, render_template, url_for, current_app
from flask_login import login_required, current_user
from app.models import Recipe, Category
from app import db, Config
from werkzeug.utils import secure_filename
import os

recipe_bp = Blueprint('recipe', __name__)

@recipe_bp.route('/new_recipe', methods=['POST'])
@login_required
def create_recipe():
    """
    This function creates a recipe
    """
    try:
        title = request.form['title']
        description = request.form['description']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        category_id = request.form['category_id']

        image_file = request.files.get('image_file')
        if image_file:
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            image_file.save(image_path)
            image_url = url_for('static', filename='uploads/' + filename)
        else:
            image_url = None

        recipe = Recipe(
            title=title,
            description=description,
            ingredients=ingredients,
            instructions=instructions,
            image_url=image_url,
            user_id=current_user.id,
            category_id=category_id
        )
        
        db.session.add(recipe)
        db.session.commit()
        return jsonify(recipe.to_dict()), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@recipe_bp.route('/create_recipe_page')
@login_required
def create_recipe_page():
    """
    This function renders the HTML template for creating a new recipe
    """
    categories = Category.query.all()
    return render_template('create_recipe.html', categories=categories)


@recipe_bp.route('/allrecipes', methods=['GET'])
def get_recipes():
    """
    This function returns all recipes
    """
    recipes = Recipe.query.all()
    return jsonify([recipe.to_dict() for recipe in recipes])

@recipe_bp.route('/recipe/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    """
    This function returns a single recipe by its id
    """
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return jsonify({'error': 'Recipe Not Found'})
    
    user = recipe.user.to_dict() if recipe.user else None
    category = recipe.category.to_dict() if recipe.category else None
    comments = [comment.to_dict() for comment in recipe.comments]

    """constructing the json response"""
    recipe_dict = recipe.to_dict()
    recipe_dict['user'] = user
    recipe_dict['category'] = category
    recipe_dict['comments'] = comments

    return jsonify(recipe_dict)
