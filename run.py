"""
This is the main file for the application.
"""
from app import create_app, db
from app.models import User

app = create_app()

"""Registering functions to be called with the shell command"""
@app.shell_context_processor
def make_shell_context():
    return {'db': db,
            'User': User}


if __name__ == '__main__':
    app.run(debug=True)
