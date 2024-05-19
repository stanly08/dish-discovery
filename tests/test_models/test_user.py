"""
This is a test module for the User model.
"""
import unittest
from datetime import datetime
from app import create_app, db
from app.models.user import User
from sqlalchemy.inspection import inspect

class TestUserModel(unittest.TestCase):
    """
    This is a class for testing the User model.
    """

    def setUp(self):
        """
        Set up the test case. Initialize the app with test config and create all tables.
        """
        print("Running test_user_model.py")
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        print(f"Tables: {tables}")


        self.client = self.app.test_client()
        self.session = db.session

    def tearDown(self):
        """
        Tear down the test case. Remove the session and drop all tables.
        """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_model(self):
        """
        This is a test method to test the User model.
        """
        user = User(username='test_user', email="test@alx.com", password="test")
        user2 = User(username='test_usr', email="mm@alx.com", password="mom")
        self.session.add(user)
        self.session.add(user2)
        self.session.commit()

        retrieved_user = User.query.filter_by(username='test_user').first()
        print(f"Retrieved user: {retrieved_user}")
        print(f"Retrieved user id: {retrieved_user.id}")
        print(f"Retrieved user created_at: {retrieved_user.created_at}")
        print(f"Retrieved user updated_at: {retrieved_user.updated_at}")

        retrieved_user2 = User.query.filter_by(username='test_usr').first()
        print(f"Retrieved user: {retrieved_user2}")
        print(f"Retrieved user id: {retrieved_user2.id}")
        print(f"Retrieved user created_at: {retrieved_user2.created_at}")
        print(f"Retrieved user updated_at: {retrieved_user2.updated_at}")
        self.assertIsNotNone(retrieved_user)
        self.assertIsInstance(retrieved_user, User)
        self.assertEqual(retrieved_user.username, 'test_user')
        self.assertEqual(retrieved_user.email, 'test@alx.com')
        self.assertTrue(retrieved_user.check_password('test'))
        self.assertFalse(retrieved_user.check_password('wrong_password'))
        self.assertEqual(retrieved_user.role_id, 1)
        self.assertIsInstance(retrieved_user.created_at, datetime)
        self.assertIsInstance(retrieved_user.updated_at, datetime)

if __name__ == '__main__':
    unittest.main()
