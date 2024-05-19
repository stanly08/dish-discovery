import unittest
from app import create_app, db
from app.models.role import Role
from sqlalchemy.inspection import inspect

class TestRoleModel(unittest.TestCase):
    """
    This is a class for testing the Role model.
    """

    def setUp(self):
        """
        Set up the test case. Initialize the app with test config and create all tables.
        """
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        self.session = db.session

    def tearDown(self):
        """
        Tear down the test case. Remove the session and drop all tables.
        """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_role_model(self):
        """
        This is a test method to test the Role model.
        """
        role = Role(name='Admin', description='Administrator role')
        role2 = Role(name='User', description='Regular user role')
        self.session.add(role)
        self.session.add(role2)
        self.session.commit()

        retrieved_role = Role.query.filter_by(name='Admin').first()
        print(f"Retrieved role: {retrieved_role}")
        print(f"Retrieved role id: {retrieved_role.id}")
        print(f"Retrieved role created_at: {retrieved_role.created_at}")
        print(f"Retrieved role updated_at: {retrieved_role.updated_at}")
        self.assertIsNotNone(retrieved_role)
        self.assertIsInstance(retrieved_role, Role)
        self.assertEqual(retrieved_role.name, 'Admin')
        self.assertEqual(retrieved_role.description, 'Administrator role')

        retrieved_role2 = Role.query.filter_by(name='User').first()
        print(f"Retrieved role: {retrieved_role2}")
        print(f"Retrieved role id: {retrieved_role2.id}")
        print(f"Retrieved role created_at: {retrieved_role2.created_at}")
        print(f"Retrieved role updated_at: {retrieved_role2.updated_at}")
        self.assertIsNotNone(retrieved_role2)
        self.assertIsInstance(retrieved_role2, Role)
        self.assertEqual(retrieved_role2.name, 'User')
        self.assertEqual(retrieved_role2.description, 'Regular user role')

if __name__ == '__main__':
    unittest.main()
