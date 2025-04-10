document.getElementById("search-input").addEventListener("focus", function () {
    document.getElementById("dropdown-container").style.display = "block";
});

// Hide dropdown when clicking outside
document.addEventListener("click", function (event) {
    let dropdown = document.getElementById("dropdown-container");
    if (!document.getElementById("search-input").contains(event.target) &&
        !dropdown.contains(event.target)) {
        dropdown.style.display = "none";
    }
});


    // Show modal
    function showModal(modalId) {
      document.getElementById(modalId).style.display = "block";
    }

    // Close modal
    function closeModal(modalId) {
      document.getElementById(modalId).style.display = "none";
    }

    // Open login modal on card click
   



    
    // Mobile Navigation Menu Toggle
  // Add toggle functionality for dropdown
  const searchInput = document.getElementById('search-input');
  const dropdown = document.getElementById('dropdown-container');

  searchInput.addEventListener('focus', () => {
      dropdown.classList.add('active');
  });

  searchInput.addEventListener('blur', () => {
      setTimeout(() => dropdown.classList.remove('active'), 200);
  });

  // Close dropdown when clicking outside
  document.addEventListener('click', (e) => {
      if (!searchInput.contains(e.target)) {
          dropdown.classList.remove('active');
      }
  });


     // Update current year automatically
     document.querySelector('.current-year').textContent = new Date().getFullYear();
    
  
    // Open chatbox after login (Spare part feature)

    
