from flask import Blueprint, request, jsonify, render_template, url_for, current_app
from flask_login import login_required, current_user
from app.models import Recipe, Category
from app import db, Config
from werkzeug.utils import secure_filename
import os

update_recipe_bp = Blueprint('update_recipe', __name__)

@update_recipe_bp.route('/recipe/<int:recipe_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_recipe(recipe_id):
    """
    This function handles the editing of a recipe.
    """
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    if request.method == 'POST':
        try:
            recipe.title = request.form['title']
            recipe.description = request.form['description']
            recipe.ingredients = request.form['ingredients']
            recipe.instructions = request.form['instructions']
            recipe.category_id = request.form['category_id']

            image_file = request.files.get('image_file')
            if image_file:
                filename = secure_filename(image_file.filename)
                image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                image_file.save(image_path)
                recipe.image_url = url_for('static', filename='uploads/' + filename)

            db.session.commit()
            return jsonify(recipe.to_dict()), 200

        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500

    categories = Category.query.all()
    return render_template('edit_recipe.html', recipe=recipe, categories=categories)
