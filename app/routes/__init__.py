from flask import Blueprint
from app.routes.home import home_bp
from app.routes.recipe import recipe_bp
from app.routes.update_recipe import update_recipe_bp
from app.routes.delete_recipe import delete_recipe_bp
from app.routes.user_profile import user_profile_bp
from app.routes.save_unsave_recipe import save_unsave_recipe_bp
from app.routes.search_recipes import search_recipes_bp

# Create a Blueprint for the routes in this folder
routes_bp = Blueprint('routes', __name__)

# Register the Blueprints for different sets of routes
routes_bp.register_blueprint(home_bp)
routes_bp.register_blueprint(recipe_bp)
routes_bp.register_blueprint(update_recipe_bp)
routes_bp.register_blueprint(delete_recipe_bp)
routes_bp.register_blueprint(user_profile_bp)
routes_bp.register_blueprint(save_unsave_recipe_bp)
routes_bp.register_blueprint(search_recipes_bp)
