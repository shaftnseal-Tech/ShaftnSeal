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

    // Fetch models for the selected maker
    fetch(`${SPARES_BASE_URL}/get_pumpmodels/${makerId}/`)
        .then(response => response.json())
        .then(data => {
            const modelSelect = document.getElementById('ModelName');
            modelSelect.innerHTML = '<option value="">Select Model</option>';
            data.forEach(model => {
                const option = document.createElement('option');
                console.log(model)
                option.value = model.id;
                option.text =option.text = `${escapeHTML(model.name)} - ${model.discharge_diameter ?? 'N/A'}`;

                modelSelect.appendChild(option);
            });

            // Show the modal form
            document.getElementById('search-form').style.display = 'block';
        })
        .catch(error => {
            console.error('Error fetching models:', error);
        });
}

// Fetch variants when a model is selected
function fetchVariants() {
    const modelId = document.getElementById('ModelName').value;
    if (!modelId) return;

    fetch(`${SPARES_BASE_URL}/get_model_varient/${modelId}/`)
        .then(response => response.json())
        .then(data => {
            const variantSelect = document.getElementById('Variant');
            variantSelect.innerHTML = '<option value="">Select Stages</option>';
            data.forEach(variant => {
                const option = document.createElement('option');
                option.value = variant.id;
                option.text = `${variant.stages} stages`;
                variantSelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error fetching variants:', error);
        });
}

function fetchModelDesigns() {
    const variantId = document.getElementById('Variant').value;
    if (!variantId) return;

    fetch(`${SPARES_BASE_URL}/get_model_design/${variantId}/`)
        .then(response => response.json())
        .then(data => {
            const ModelDesignSelect = document.getElementById('ModelDesign');
            ModelDesignSelect.innerHTML = '<option value="">Select Model Design</option>';
            data.forEach(design => {
                const option = document.createElement('option');
                option.value = design.id;
                option.text = `${design.model_design}`;
                ModelDesignSelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error in fetching model designs:', error);
        });
}
// Redirect to parts page with selected model and variant UUIDs
function searchParts() {
    const model_Id = document.getElementById('ModelName').value;
    const variant_Id = document.getElementById('Variant').value;
    const ModelDesign_Id = document.getElementById('ModelDesign').value;

    if (!model_Id || !variant_Id || !ModelDesign_Id) {
        alert('Please select all Model and Variant and ModelDesign.');
        return;
    }

    window.location.href = `${SPARES_BASE_URL}/get_parts/${model_Id}/${variant_Id}/${ModelDesign_Id}`;
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