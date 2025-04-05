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
    let isLoggedIn = sessionStorage.getItem("isLoggedIn") === "true";

// Handle card clicks with login validation
document.querySelectorAll(".card").forEach(card => {
    card.addEventListener("click", function (event) {
        event.preventDefault();

        let targetUrl = card.getAttribute("data-url");
        window.location.href = targetUrl;

     
    });
});
     // Close modal when clicking outside
     window.onclick = function(event) {
        let loginModal = document.getElementById("login-form");
        let registerModal = document.getElementById("registration-form");
        if (event.target === loginModal) {
            closeModal("login-form");
        } else if (event.target === registerModal) {
            closeModal("registration-form");
        }
    };
    
    function login() {
        isLoggedIn = true;
        sessionStorage.setItem("isLoggedIn", "true"); // Use sessionStorage for consistency
        closeModal("login-form"); // Ensure modal closes
    
        let redirectUrl = sessionStorage.getItem("redirectAfterLogin");
        if (redirectUrl) {
            sessionStorage.removeItem("redirectAfterLogin");
            window.location.href = redirectUrl; // Navigate to stored URL
        } else {
            window.location.href = "dashboard.html"; // Default page after login
        }
    }
    
    ///logout  
    function logout() {
        // Clear session storage or local storage (if used for authentication)
        sessionStorage.clear();
        localStorage.clear();
        
        // Redirect to login page or home page
        window.location.href = "index.html";
    }

   
    // Validate and submit form
    function submitForm() {
        const customerName = document.getElementById("customerName").value;
        const address = document.getElementById("address").value;
        const pinCode = document.getElementById("pincode").value;
        const phoneNo = document.getElementById("phoneNo").value;
        let emailInput = document.getElementById("email");
        let emailError = document.getElementById("emailError");
        let emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        // Validate mandatory fields
        if (!customerName || !address || !pinCode || !phoneNo) {
            alert("Please fill in all the required fields.");
            return;
        }
            // validation phone number
    if (!/^\d{10}$/.test(phoneNo)) {
        alert("Please enter a valid 10-digit phone number.");
        return;
    }
    // validation customer code
    if (!/^\d{6}$/.test(customerCode)) {
        alert("Customer Code must be exactly 6 digits.");
        return;
    }
     // validation email format
    
     if (!emailPattern.test(emailInput.value)) {
        emailError.textContent = "Invalid email format!";
        emailInput.style.borderColor = "red";
    } else {
        emailError.textContent = "";
        emailInput.style.borderColor = "green";
        alert("Email is valid!");
    }
        // Generate Customer Code and GST Number
        const customerCode = generateCustomerCode();
        const gstNumber = generateGSTNumber(pinCode);
    
        // Display generated info
        document.getElementById("customerCode").textContent = customerCode;
        document.getElementById("gstNumber").textContent = gstNumber;
        document.getElementById("generatedInfo").style.display = "block";
        
    }
    //Generate customer detail
    function generateCustomerDetails() {
        const pincode = document.getElementById('pincode').value.trim();
        const customerNo = document.getElementById('Customerno').value.trim();

        if (!pincode || !customerNo) {
            alert("Please enter both Customer Number and PIN Code.");
            return;
        }

        // Generate Customer Code
        const customerCode = `CUST-${customerNo}-${Math.floor(1000 + Math.random() * 9000)}`;

        // Generate GST Number format: CUST-XXXX-PIN-GST
        const gstNumber = `CUST-${customerNo}-${pincode}-GST`;

        // Display generated info
        document.getElementById('customerCode').innerText = customerCode;
        document.getElementById('gstNumber').innerText = gstNumber;
        document.getElementById('generatedInfo').style.display = 'block';
    }
    // Mobile Navigation Menu Toggle
  // Add toggle functionality for dropdown
  const searchInput = document.getElementById('search-input');
  const dropdown = document.getElementById('dropdown-container');
  
  // Show dropdown on focus or typing
  const showDropdown = () => {
    if (searchInput.value.trim() !== '' || document.activeElement === searchInput) {
      dropdown.classList.add('active');
      dropdown.style.display = 'block'; // fallback if not using class-based display
    }
  };
  
  // Hide dropdown with delay (for click targets inside dropdown)
  const hideDropdown = () => {
    setTimeout(() => {
      dropdown.classList.remove('active');
      dropdown.style.display = 'none';
    }, 200);
  };
  
  searchInput.addEventListener('focus', showDropdown);
  searchInput.addEventListener('input', showDropdown);
  searchInput.addEventListener('blur', hideDropdown);
  
  // Close dropdown when clicking outside
  document.addEventListener('click', (e) => {
    if (!document.querySelector('.search-icon-container').contains(e.target)) {
      dropdown.classList.remove('active');
      dropdown.style.display = 'none';
    }
  });
  

     // Update current year automatically
     document.querySelector('.current-year').textContent = new Date().getFullYear();
    
    //registration form open
    window.onclick = function(event) {
        let modal = document.getElementById("registration-form");
        if (event.target === modal) {
            showModal("registration-form")
            modal.style.display = "none";
        }
    }
    // Open chatbox after login (Spare part feature)
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("spares-card").addEventListener("click", function (event) {
        event.preventDefault();
        checkLoginAndNavigate("sparepage.html");
    });
});
    
