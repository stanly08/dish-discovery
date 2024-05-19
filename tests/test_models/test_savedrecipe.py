import unittest
from app.models.savedrecipe import SavedRecipe
from app.models.user import User
from app.models.recipe import Recipe
from app import create_app, db

class TestSavedRecipeModel(unittest.TestCase):
    """
    Test cases for the SavedRecipe model.
    """

    def setUp(self):
        """
        Set up the test case. Initialize the app with test config and create all tables.
        """
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """
        Tear down the test case. Remove the session and drop all tables.
        """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_saved_recipe_creation(self):
        """
        Test creating a new saved recipe.
        """
        user = User(username='user1', email='user1@example.com', password='password1')
        db.session.add(user)
        db.session.commit()

        recipe = Recipe(title='Recipe 1', ingredients='Ingredient 1', 
                        instructions='Step 1', image_url='https://example.com/image1.jpg',
                        user_id=user.id)
        db.session.add(recipe)
        db.session.commit()

        saved_recipe = SavedRecipe(user_id=user.id, recipe_id=recipe.id)
        db.session.add(saved_recipe)
        db.session.commit()

        retrieved_saved_recipe = SavedRecipe.query.filter_by(user_id=user.id, recipe_id=recipe.id).first()

        self.assertIsNotNone(retrieved_saved_recipe)
        self.assertEqual(retrieved_saved_recipe.user_id, user.id)
        self.assertEqual(retrieved_saved_recipe.recipe_id, recipe.id)

if __name__ == '__main__':
    unittest.main()
