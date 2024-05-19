import unittest
from app import create_app, db
from app.models.recipe import Recipe
from app.models.user import User

class TestRecipeModel(unittest.TestCase):
    """
    This class contains unit tests for the Recipe model.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test class. Initialize the app with test config and create all tables.
        """
        cls.app = create_app('test')
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the test class. Remove the app context and drop all tables.
        """
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def setUp(self):
        """
        Set up each test case. Create a user and add it to the database.
        """
        self.user = User(username='test_user', email='test@example.com', password='test_password')
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        """
        Tear down each test case. Remove the user from the database.
        """
        pass

    def test_recipe_creation(self):
        """
        Test recipe creation and retrieval.
        """
        recipe = Recipe(title='Test Recipe', ingredients='Ingredient 1, Ingredient 2', instructions='Step 1, Step 2', image_url='test_image_url', user_id=self.user.id)
        db.session.add(recipe)
        db.session.commit()

        print(f"Recipe: {recipe}")
        print(f"Recipe id: {recipe.id}")
        print(f"Recipe created_at: {recipe.created_at}")
        print(f"Recipe updated_at: {recipe.updated_at}")
        print(f"Recipe user: {recipe.user}" )

        retrieved_recipe = Recipe.query.filter_by(title='Test Recipe').first()
        self.assertIsNotNone(retrieved_recipe)
        self.assertEqual(retrieved_recipe.title, 'Test Recipe')
        self.assertEqual(retrieved_recipe.ingredients, 'Ingredient 1, Ingredient 2')
        self.assertEqual(retrieved_recipe.instructions, 'Step 1, Step 2')
        self.assertEqual(retrieved_recipe.image_url, 'test_image_url')
        self.assertEqual(retrieved_recipe.user_id, self.user.id)

if __name__ == '__main__':
    unittest.main()
