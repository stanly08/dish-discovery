from flask import Blueprint, request, jsonify
from app.models import Recipe

search_recipes_bp = Blueprint('search_recipes', __name__)


@search_recipes_bp.route('/search', methods=['GET'])
def search_recipes():
    """
    This function handles searching for recipes.
    """
    query = request.args.get('q')
    if not query:
        return jsonify({'error': 'Query parameter is required'}), 400

    recipes = Recipe.query.filter(Recipe.title.ilike(f'%{query}%') |
                                  Recipe.description.ilike(f'%{query}%') |
                                  Recipe.ingredients.ilike(f'%{query}%')).all()

    return jsonify([recipe.to_dict() for recipe in recipes])
