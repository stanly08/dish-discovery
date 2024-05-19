import unittest
from app.models.comment import Comment
from app.models.user import User
from app.models.recipe import Recipe
from app.models.category import Category
from app import create_app, db

class TestCommentModel(unittest.TestCase):
    """
    Test cases for the Comment model.
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

    def test_comment_creation(self):
        """
        Test creating a new comment.
        """
        user1 = User(username='user1', email='user1@example.com', password='password1')
        user2 = User(username='user2', email='user2@example.com', password='password2')
        db.session.add_all([user1, user2])
        db.session.commit()

        category = Category(name='Test Category')
        db.session.add(category)
        db.session.commit()

        recipe1 = Recipe(title='Recipe 1', ingredients='Ingredient 1', 
                         instructions='Step 1', image_url='https://example.com/image1.jpg',
                         user_id=user1.id, category_id=category.id)
        recipe2 = Recipe(title='Recipe 2', ingredients='Ingredient 2', 
                         instructions='Step 2', image_url='https://example.com/image2.jpg',
                         user_id=user2.id, category_id=category.id)
        db.session.add_all([recipe1, recipe2])
        db.session.commit()

        comment = Comment(content='Test comment', user_id=user1.id, recipe_id=recipe2.id)
        db.session.add(comment)
        db.session.commit()

        retrieved_comment = Comment.query.filter_by(content='Test comment').first()

        self.assertIsNotNone(retrieved_comment)
        self.assertEqual(retrieved_comment.content, 'Test comment')
        self.assertEqual(retrieved_comment.user_id, user1.id)
        self.assertEqual(retrieved_comment.recipe_id, recipe2.id)

if __name__ == '__main__':
    unittest.main()
