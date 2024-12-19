document.addEventListener('DOMContentLoaded', function () {
  // Get the query parameters
  const urlParams = new URLSearchParams(window.location.search);
  const imageUrl = urlParams.get('image');

  // If an image URL exists, add it to the image container
  if (imageUrl) {
      const imageContainer = document.getElementById('image-container');
      const imgElement = document.createElement('img');
      imgElement.src = imageUrl;
      imgElement.alt = "Selected Image";
      imgElement.classList.add('responsive-image'); // Add CSS class for styling
      imageContainer.appendChild(imgElement);
  }
});
