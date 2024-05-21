"""
This is the file for the recipe routes
"""
from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required, current_user
from app.models.recipe import Recipe
from app import db

recipe_bp = Blueprint('recipe', __name__)

@recipe_bp.route('/new_recipe', methods=['POST'])
@login_required
def create_recipe():
    """
    This function creates a recipe
    """
    print("function call")
    try:
        data = request.get_json()
        print("data requested")
        image_url = data.get('image_url', None)
        category_id = data.get('category_id', None)
        print(image_url)
        print(category_id)
        recipe = Recipe(title=data['title'],
                        description=data['description'],
                        ingredients=data['ingredients'],
                        instructions=data['instructions'],
                        image_url=image_url,
                        user_id=current_user.id,
                        category_id=category_id)
        print(recipe.title)
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
    return render_template('create_recipe.html')


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

