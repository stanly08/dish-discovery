# Dish Discovery

Dish discovery is a web application that allows users to create and share their own recipes to the database.Users can sign up, log in, create recipes, and view recipes created by others. The application also supports commenting on recipes and saving favorite recipes.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Manual Database Migrations](#manual-database-migrations)
  - [Using MySQL](#using-mysql)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Authors](#authors)
- [License](#license)

## Features

- User Authentication: Sign up, log in and log out functionalities
- Recipe Management: create, view, and delete recipes
- Comments: Users can comment on the recipes
- Save and Unsave favorite recipes
- User profiles: users can view their details and the recipes they have done
- Dynamic Recipe Display: Recipes are dynamically loading using JSON and Javascript

## Getting Started

### Prerequisites

- Python 3.8+
- Flask
- SQLite (default) or any other SQLAlchemy-supported database

### Installation

1. Clone the repository

   ```sh
   https://github.com/stanly08/dish-discovery.git
   ```

2. Navigate to the project directory:

   ```sh
   cd dish-discovery
   ```

3. Create a virtual environment:

   ```
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - on Windows:

   ```sh
   venv\Scripts\activate
   ```

   - on macOS and Linux:

   ```sh
   source venv/bin/activate
   ```

5. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

6. Set up the database:

   - Currently using SQLlite db

   ```sh
   ./database.sh
   ```

7. Start the Flask development Server:

   ```sh
   flask run
   ```

### Manual Database Migrations

1. Initialize the migrations directory

```sh
flask db init
```

2. Create an initial migration

```sh
flask db migrate -m "initial migration"
```

3. Apply the migration

```sh
flask db upgrade
```

## Using MySQL

To use Mysql

```sh
    pip install flask-mysqldb
```

```sh
    pip install mysqlclient
```

Update the Config.py

```sh
    MYSQL_HOST = os.environ.get('MYSQL_HOST') or 'localhost'
    MYSQL_USER = os.environ.get('MYSQL_USER') or 'your-username'
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or 'your-password'
    MYSQL_DB = os.environ.get('MYSQL_DB') or 'your-database'
    MYSQL_CURSORCLASS = 'DictCursor'

    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlclient://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
```

## Project Structure

```sh
dish-discovery/
│
├── app/
│ ├── **init**.py
│ ├── forms/
│ │ ├── login.py
│ ├── models/
│ │ ├── **init**.py
│ │ ├── user.py
│ │ ├── recipe.py
│ │ ├── comment.py
│ ├── routes/
│ │ ├── **init**.py
│ │ ├── home.py
│ │ ├── recipe.py
│ ├── static/
│ ├── templates/
│ │ ├── base.html
│ │ ├── index.html
│ │ ├── login.html
│ │ ├── register.html
│
├── migrations/
│
├── tests/
│ ├── test_routes.py
│ ├── test_models.py
│
├── .env.example
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

## Contributing

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -am 'Add new feature').
5. Push to the branch (git push origin feature-branch).
6. Create a new Pull Request.

## Authors

1. Jackline Wanjiku
2. Edwin K. Orioki
3. Stanly Anasi

## License

This project is licensed under the MIT License.
See the LICENSE file for details.
