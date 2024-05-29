function addToFavorites(itemId) {
    let recipe = document.getElementById(itemId);
    
    let recipeTitle = recipe.querySelector('.recipe-title').innerText;
    let recipeDescription = recipe.querySelector('.recipe-description').innerText;
    let recipeImageSrc = recipe.querySelector('.image').src;
    
    let favoriteRecipe = {
        title: recipeTitle,
        description: recipeDescription,
        imageSrc: recipeImageSrc
    };

    let favorites = JSON.parse(localStorage.getItem('favorites')) || [];
    favorites.push(favoriteRecipe);
    localStorage.setItem('favorites', JSON.stringify(favorites));
    
    let favoriteButton = recipe.querySelector('.glyphicon-heart-empty');
    favoriteButton.classList.remove('glyphicon-heart-empty');
    favoriteButton.classList.add('glyphicon-heart');
}

var fullImgBox = document.getElementById("fullImgBox");
var fullImg = document.getElementById("fullImg");

function openFullImg(pic){
    fullImgBox.style.display = "flex";
    fullImg.src = pic;
}


function getRandomRecipe() {
    const recipeIds = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7', 'item8', 'item9'];

    const randomRecipeId = recipeIds[Math.floor(Math.random() * recipeIds.length)];

    const randomRecipe = document.getElementById(randomRecipeId);

    const featuredRecipeContainer = document.getElementById('featured-recipe');

    featuredRecipeContainer.innerHTML = randomRecipe.innerHTML;
  }

  window.onload = getRandomRecipe;
