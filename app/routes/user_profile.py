from flask import Blueprint, jsonify, render_template
from app.models import User, Recipe

user_profile_bp = Blueprint('user_profile', __name__)


@user_profile_bp.route('/user/<int:user_id>', methods=['GET'])
def user_profile(user_id):
    """
    This function returns the user's profile and their recipes.
    """
    user = User.query.get_or_404(user_id)
    user_recipes = Recipe.query.filter_by(user_id=user.id).all()

    return render_template('user_profile.html', user=user, user_recipes=user_recipes)
