from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.models import Recipe, SavedRecipe
from app import db

save_unsave_recipe_bp = Blueprint('save_unsave_recipe', __name__)


@recipe_bp.route('/recipe/<int:recipe_id>/save', methods=['POST'])
@login_required
def save_recipe(recipe_id):
    """
    This function handles saving a recipe.
    """
    recipe = Recipe.query.get_or_404(recipe_id)
    saved_recipe = SavedRecipe.query.filter_by(user_id=current_user.id, recipe_id=recipe_id).first()
    if saved_recipe:
        return jsonify({'error': 'Recipe already saved'}), 400

    try:
        saved_recipe = SavedRecipe(user_id=current_user.id, recipe_id=recipe_id)
        db.session.add(saved_recipe)
        db.session.commit()
        return jsonify({'message': 'Recipe saved successfully'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@recipe_bp.route('/recipe/<int:recipe_id>/unsave', methods=['DELETE'])
@login_required
def unsave_recipe(recipe_id):
    """
    This function handles unsaving a recipe.
    """
    saved_recipe = SavedRecipe.query.filter_by(user_id=current_user.id, recipe_id=recipe_id).first()
    if not saved_recipe:
        return jsonify({'error': 'Recipe not saved'}), 400

    try:
        db.session.delete(saved_recipe)
        db.session.commit()
        return jsonify({'message': 'Recipe unsaved successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
