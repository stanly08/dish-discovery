document.addEventListener("DOMContentLoaded", (event) => {
  const tabButtons = document.querySelectorAll(".tab-button");
  const tabContents = document.querySelectorAll(".tab-pane");

  tabButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const tabId = button.getAttribute("data-tab");
      activateTab(tabId);
    });
  });

  function activateTab(tabId) {
    tabContents.forEach((tab) => {
      if (tab.id === tabId) {
        tab.classList.add("active");
      } else {
        tab.classList.remove("active");
      }
    });

    tabButtons.forEach((button) => {
      if (button.getAttribute("data-tab") === tabId) {
        button.classList.add("active");
      } else {
        button.classList.remove("active");
      }
    });
  }

  document.querySelectorAll(".next-tab-btn").forEach((button) => {
    button.addEventListener("click", () => {
      const tabId = button.getAttribute("data-tab");
      activateTab(tabId);
    });
  });

  document.querySelectorAll(".prev-tab-btn").forEach((button) => {
    button.addEventListener("click", () => {
      const tabId = button.getAttribute("data-tab");
      activateTab(tabId);
    });
  });

  // Initialize CKEditor for text areas
  CKEDITOR.replace("description");
  CKEDITOR.replace("ingredients");
  CKEDITOR.replace("instructions");

  /** Form handling logic **/
  const categoryElement = document.getElementById("category");
  if (categoryElement) {
    categoryElement.addEventListener("change", function () {
      const selectedCategory = this.options[this.selectedIndex];
      const categoryIdElement = document.getElementById("category_id");
      if (categoryIdElement) {
        categoryIdElement.value = selectedCategory.value;
      }
    });
  }

  const recipeForm = document.getElementById("recipeForm");
  if (recipeForm) {
    recipeForm.addEventListener("submit", function (event) {
      event.preventDefault();

      // Update CKEditor instances before submitting the form
      for (let instance in CKEDITOR.instances) {
        CKEDITOR.instances[instance].updateElement();
      }

      const formData = new FormData(this);

      fetch("/new_recipe", {
        method: "POST",
        body: formData,
      })
        .then((response) => {
          const contentType = response.headers.get("content-type");
          if (contentType && contentType.includes("application/json")) {
            return response.json();
          } else {
            return response.text().then((text) => {
              throw new Error("Expected JSON response but got " + contentType + "\nResponse text: " + text);
            });
          }
        })
        .then((data) => {
          console.log("Success:", data);
          alert("Recipe created successfully!");
          window.location.href = `/recipe/${data.id}`;
        })
        .catch((error) => {
          console.error("Error:", error);
          alert("An error occurred while creating the recipe: " + error.message);
        });
    });
  }

  /* Auto-resize textareas */
  const textareas = document.querySelectorAll(".auto-resize");
  textareas.forEach((textarea) => {
    textarea.addEventListener("input", autoResize);
  });

  function autoResize() {
    this.style.height = "auto";
    this.style.height = this.scrollHeight + "px";
  }
});
