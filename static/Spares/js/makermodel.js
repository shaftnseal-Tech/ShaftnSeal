const SPARES_BASE_URL = '/Spares';
 
function escapeHTML(str) {
    const div = document.createElement('div');
    div.innerText = str;
    return div.innerHTML;
}
 
// Show dropdown on focus
function showDropdown() {
    const dropdown = document.getElementById('dropdown-container');
    dropdown.style.display = 'block';
}
 
// Filter dropdown links on keyup
function filterDropdown() {
    const input = document.getElementById('search');
    const filter = input.value.toLowerCase();
    const dropdown = document.getElementById('dropdown-container');
    const links = dropdown.getElementsByTagName('a');
 
    for (let i = 0; i < links.length; i++) {
        const txtValue = links[i].textContent || links[i].innerText;
        links[i].style.display = txtValue.toLowerCase().includes(filter) ? '' : 'none';
    }
}
 
// Handle selection of a maker
function selectMaker(makerId, makerName) {
    document.getElementById('search').value = makerName;
    document.getElementById('dropdown-container').style.display = 'none';

    // Fetch models
    fetch(`${SPARES_BASE_URL}/get_pumpmodels/${makerId}/`)
        .then(response => response.json())
        .then(data => {
            const modelSelect = document.getElementById('ModelName');
            modelSelect.innerHTML = '<option value="">Select Model</option>';
            data.forEach(model => {
                const option = document.createElement('option');
                option.value = model.id;
                option.text = escapeHTML(model.name);
                modelSelect.appendChild(option);
            });

            // Show modal by adding active class
            document.getElementById('search-form').classList.add('active');
        })
        .catch(error => {
            console.error('Error fetching models:', error);
        });
}

function closeModal(id) {
    document.getElementById(id).classList.remove('active');
}

 
// Fetch variants when a model is selected
function fetchVariants() {
    const modelId = document.getElementById('ModelName').value;
    if (!modelId) return;
 
    fetch(`${SPARES_BASE_URL}/get_model_varient/${modelId}/`)
        .then(response => response.json())
        .then(data => {
            const variantSelect = document.getElementById('Variant');
            variantSelect.innerHTML = '<option value="">Select Variant</option>';
            data.forEach(variant => {
                const option = document.createElement('option');
                option.value = variant.id;
                option.text = `${variant.discharge_diameter}mm - ${variant.stages} stages`;
                variantSelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error fetching variants:', error);
        });
}
 
// Redirect to parts page with selected model and variant UUIDs
function searchParts() {
    const model_Id = document.getElementById('ModelName').value;
    const variant_Id = document.getElementById('Variant').value;
 
    if (!model_Id || !variant_Id) {
        alert('Please select both Model and Variant.');
        return;
    }
 
    window.location.href = `${SPARES_BASE_URL}/get_parts/${model_Id}/${variant_Id}/`;
}
 
 
 
// Close modal
function closeModal(id) {
    document.getElementById(id).style.display = 'none';
}
 
// Optional: Hide dropdown when clicking outside
document.addEventListener('click', function (event) {
    const dropdown = document.getElementById('dropdown-container');
    const searchBox = document.getElementById('search');
    if (!dropdown.contains(event.target) && event.target !== searchBox) {
        dropdown.style.display = 'none';
    }
});
 