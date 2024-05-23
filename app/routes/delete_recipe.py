from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import Recipe
from app import db

delete_recipe_bp = Blueprint('delete_recipe', __name__)


@recipe_bp.route('/recipe/<int:recipe_id>/delete', methods=['DELETE'])
@login_required
def delete_recipe(recipe_id):
    """
    This function handles the deletion of a recipe.
    """
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    try:
        db.session.delete(recipe)
        db.session.commit()
        return jsonify({'message': 'Recipe deleted successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
