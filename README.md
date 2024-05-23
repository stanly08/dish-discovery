# Dish Discovery

Dish discovery is a web application that allows users to create and share their own recipes to the database.

## Features

- User Authentication: Sign up, log in and log out functionalities
- Recipe Management: create, view, and manage recipes
- Comments: Users can comment on the recipes
- Dynamic Recipe Display: Recipes are dynamically loading using JSON and Javascript

## Installation

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
   python -m venv venv
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

8. Naviage to the home page `http://127.0.0.1:5000'

## API Endpoints

### 1. Create a Recipe

- **URL**: `/new_recipe`
- **Method**: `POST`
- **Headers**: `Content-Type: application/json`
- **Body**:
  ```json
  {
    "title": "Recipe Title",
    "description": "Recipe Description",
    "ingredients": "List of ingredients",
    "instructions": "Cooking instructions",
    "image_url": "http://example.com/image.jpg",
    "category_id": 1
  }
  ```
- **Response**: `201 Created` with the created recipe in JSON format.

### 2. Get All Recipes

- **URL**: `/allrecipes`
- **Method**: `GET`
- **Response**: `200 OK` with a list of recipes in JSON format.

### Get a Single Recipe

- **URL**: `/recipe/<recipe_id>`
- **Method**: `GET`
- **Response**: `200 OK` with the recipe details in JSON format, or `404 Not Found` if the recipe does not exist.

### 3. Delete a Recipe

**URL:** `/recipe/<int:recipe_id>/delete`  
**Method:** `DELETE`  
**Authentication:** Required

Deletes a specific recipe.

#### Response

- **Success:**
  - Status Code: `200`
  - Body: `{"message": "Recipe deleted successfully"}`
- **Failure:**
  - Status Code: `403` if unauthorized
  - Status Code: `404` if recipe not found
  - Status Code: `500` if server error

### 4. Save a Recipe

**URL:** `/recipe/<int:recipe_id>/save`  
**Method:** `POST`  
**Authentication:** Required

Saves a specific recipe for the current user.

#### Response

- **Success:**
  - Status Code: `201`
  - Body: `{"message": "Recipe saved successfully"}`
- **Failure:**
  - Status Code: `400` if recipe already saved
  - Status Code: `404` if recipe not found
  - Status Code: `500` if server error

### 5. Unsave a Recipe

**URL:** `/recipe/<int:recipe_id>/unsave`  
**Method:** `DELETE`  
**Authentication:** Required

Unsaves a specific recipe for the current user.

#### Response

- **Success:**
  - Status Code: `200`
  - Body: `{"message": "Recipe unsaved successfully"}`
- **Failure:**
  - Status Code: `400` if recipe not saved
  - Status Code: `404` if recipe not found
  - Status Code: `500` if server error

### 6. Search Recipes

**URL:** `/search`  
**Method:** `GET`

Searches for recipes based on a query parameter.

#### Query Parameters

- `q`: The search query (required)

#### Response

- **Success:**
  - Status Code: `200`
  - Body: List of recipes matching the query
- **Failure:**
  - Status Code: `400` if query parameter is missing

### 7. Edit a Recipe

**URL:** `/recipe/<int:recipe_id>/edit`  
**Method:** `GET` or `POST`  
**Authentication:** Required

Edits a specific recipe. The form submission should include the updated fields.

#### Response

- **Success:**
  - Status Code: `200`
  - Body: Updated recipe details
- **Failure:**
  - Status Code: `403` if unauthorized
  - Status Code: `404` if recipe not found
  - Status Code: `500` if server error

### 8. View User Profile

**URL:** `/user/<int:user_id>`  
**Method:** `GET`

Returns the profile and recipes of a specific user.

#### Response

- **Success:**
  - Status Code: `200`
  - Body: User profile and their recipes
- **Failure:**
  - Status Code: `404` if user not found

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

## Authors

1. Jackline Wanjiku
2. Edwin K. Orioki
3. Stanly Anasi
