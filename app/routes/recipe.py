"""
This is the file for the recipe routes
"""
from flask import Blueprint, request, jsonify, render_template, url_for, current_app, redirect
from flask_login import login_required, current_user
from app.models import Recipe, Category, Comment
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

        response_data = recipe.to_dict()
        response_data['id'] = Recipe.query.order_by(Recipe.id.desc()).first().id
        
        db.session.add(recipe)
        db.session.commit()
        return jsonify(response_data), 201
    
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

    return render_template('recipe.html', recipe=recipe_dict)


@recipe_bp.route('/recipe/<int:recipe_id>/comment', methods=['POST'])
@login_required
def add_comment(recipe_id):
    content = request.form['content']
    comment = Comment(content=content, user_id=current_user.id, recipe_id=recipe_id)
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('recipe.get_recipe', recipe_id=recipe_id))

@recipe_bp.route('/recipe/<int:recipe_id>/edit', methods=['POST'])
@login_required
def edit_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if recipe.user_id != current_user.id:
        return render_template('error.html', message='You do not have permission to edit this recipe'), 403

    recipe.title = request.form['title']
    recipe.description = request.form['description']
    recipe.ingredients = request.form['ingredients']
    recipe.instructions = request.form['instructions']
    db.session.commit()
    return redirect(url_for('recipe.get_recipe', recipe_id=recipe_id))

@recipe_bp.route('/recipe/<int:recipe_id>/delete', methods=['POST'])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if recipe.user_id != current_user.id:
        return render_template('error.html', message='You do not have permission to delete this recipe'), 403

    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for('home.index'))


