from flask import Blueprint, jsonify
from app.models import User, Recipe

user_profile_bp = Blueprint('user_profile', __name__)


@user_profile_bp.route('/user/<int:user_id>', methods=['GET'])
def user_profile(user_id):
    """
    This function returns the user's profile and their recipes.
    """
    user = User.query.get_or_404(user_id)
    recipes = Recipe.query.filter_by(user_id=user.id).all()
    user_data = user.to_dict()
    user_data['recipes'] = [recipe.to_dict() for recipe in recipes]

    return jsonify(user_data)
