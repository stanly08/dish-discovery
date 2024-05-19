"""
This is a test module for the User model.
"""
import unittest
from app.models.user import User
from app.models.base import BaseModel
from datetime import datetime

class TestUserModel(unittest.TestCase):
    """
    This is a class for testing
    the User model.
    """
    def test_user_model(self):
        """
        This is a test method to test the User model.
        """
        user = User(username='test_user', email="test@alx.com", password="test")
        self.assertIsInstance(user, BaseModel)
        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.email, 'test@alx.com')
        self.assertTrue(user.check_password('test'))
        self.assertFalse(user.check_password('wrong_password'))
        self.assertEqual(user.role_id, 1)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)

if __name__ == '__main__':
    unittest.main()
