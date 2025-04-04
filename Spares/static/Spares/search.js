document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector(".form-container form");

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent the default form submission
        
        // Optionally, store form data (for backend use)
        const formData = {
            ModalName: document.getElementById("ModalName").value,
            Size: document.getElementById("Size").value,
            Stages: document.getElementById("Stages").value,
           
        };

        console.log("Form Submitted:", formData); // You can replace this with an API call

        // Close Modal
        closeModal("search-form");

        // Navigate to home page
        window.location.href = "chatbot.html";
    });
});

function showModal(modalId) {
        document.getElementById(modalId).style.display = 'flex';
    }

    function closeModal(modalId) {
        document.getElementById(modalId).style.display = 'none';
    }

  
    function showDropdown() {
        document.getElementById("dropdown-container").style.display = "block";
    }

    function selectItem(value) {
        document.getElementById("search").value = value;
        document.getElementById("dropdown-container").style.display = "none";
    }

   
    // Hide dropdown when clicking outside
    document.addEventListener("click", function(event) {
        var searchContainer = document.querySelector(".search-container");
        if (!searchContainer.contains(event.target)) {
            document.getElementById("dropdown-container").style.display = "none";
        }
    });
    const modalOptions = ["HDA", "HG",];
    const sizeOptions = ["50", "65", "80","100","125"];
    const stageOptions = ["11", "12", "13"];

    // Function to populate dropdown
    function populateDropdown(selectId, options) {
        const select = document.getElementById(selectId);
        options.forEach(option => {
            const opt = document.createElement("option");
            opt.value = option;
            opt.textContent = option;
            select.appendChild(opt);
        });
    }

    // Populate all dropdowns
    populateDropdown("ModalName", modalOptions);
    populateDropdown("Size", sizeOptions);
    populateDropdown("Stages", stageOptions);


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