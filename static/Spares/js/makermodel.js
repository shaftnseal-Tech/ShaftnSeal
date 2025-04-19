function sendMessage() {
    const inputField = document.getElementById('user-input');
    const userMessage = inputField.value.trim();
    const chatWindow = document.getElementById('chat-window');

    if (!userMessage) return;

    // Show user's message
    const userMessageDiv = document.createElement('div');
    userMessageDiv.className = 'user-message';
    userMessageDiv.innerText = userMessage;
    chatWindow.appendChild(userMessageDiv);

    // Scroll chat window to bottom
    chatWindow.scrollTop = chatWindow.scrollHeight;

    // Process the input
    chatbotResponse(userMessage);

    // Clear input field
    inputField.value = '';
}

function chatbotResponse(message) {
    const chatWindow = document.getElementById('chat-window');

    let responseText = '';
    const tableRows = document.querySelectorAll('#all-parts-list tr');

    let found = false;

    tableRows.forEach(row => {
        const partNo = row.cells[0].textContent.toLowerCase();
        const partName = row.cells[1].textContent.toLowerCase();

        if (partNo.includes(message.toLowerCase()) || partName.includes(message.toLowerCase())) {
            found = true;
            row.style.backgroundColor = '#ffff99'; // Highlight the row
            row.scrollIntoView({ behavior: 'smooth', block: 'center' });
        } else {
            row.style.backgroundColor = ''; // Reset other rows
        }
    });

    if (found) {
        responseText = `Here is the part you are looking for!`;
    } else {
        responseText = `Sorry, I couldn't find a part with "${message}". Please try another name or number.`;
    }

    // Show chatbot response
    const botMessageDiv = document.createElement('div');
    botMessageDiv.className = 'chatbot-message';
    botMessageDiv.innerText = responseText;
    chatWindow.appendChild(botMessageDiv);

    chatWindow.scrollTop = chatWindow.scrollHeight;
}

    const SPARES_BASE_URL = '/Spares';

    function showDropdown() {
        document.getElementById('dropdown-container').style.display = 'block';
    }

    function filterDropdown() {
        const input = document.getElementById('search').value.toUpperCase();
        const container = document.getElementById('dropdown-container');
        const links = container.getElementsByTagName('a');

        for (let i = 0; i < links.length; i++) {
            const txtValue = links[i].textContent || links[i].innerText;
            links[i].style.display = txtValue.toUpperCase().indexOf(input) > -1 ? "" : "none";
        }
    }

    function closeModal(modalId) {
        document.getElementById(modalId).style.display = 'none';
    }

    function selectMaker(makerId, makerName) {
        document.getElementById('search').value = makerName;
        document.getElementById('dropdown-container').style.display = 'none';

        fetch(`${SPARES_BASE_URL}/get_pumpmodels/${makerId}/`)
            .then(response => response.json())
            .then(models => {
                const modelSelect = document.getElementById('ModelName');
                modelSelect.innerHTML = '<option value="">Select Model</option>';
                models.forEach(model => {
                    modelSelect.innerHTML += `<option value="${model.id}">${model.name}</option>`;
                });

                document.getElementById('search-form').style.display = 'flex';
            })
            .catch(error => {
                console.error('Error fetching models:', error);
                alert('Failed to load pump models.');
            });
    }

    function fetchVariants() {
        const modelId = document.getElementById('ModelName').value;
        if (!modelId) return;

        fetch(`${SPARES_BASE_URL}/get_model_varient/${modelId}/`)
            .then(response => response.json())
            .then(variants => {
                const variantSelect = document.getElementById('Variant');
                variantSelect.innerHTML = '<option value="">Select Variant</option>';
                variants.forEach(variant => {
                    const text = `Dia: ${variant.discharge_diameter}mm - Stages: ${variant.stages}`;
                    variantSelect.innerHTML += `<option value="${variant.id}">${text}</option>`;
                });
            })
            .catch(error => {
                console.error('Error fetching variants:', error);
                alert('Failed to load model variants.');
            });
    }

    function searchParts() {
    const modelId = document.getElementById('ModelName').value;
    const variantId = document.getElementById('Variant').value;

    if (!modelId || !variantId) {
        alert('Please select both Model and Variant.');
        return;
    }

    fetch(`${SPARES_BASE_URL}/get_parts/${modelId}/${variantId}/`)
        .then(response => response.json())
        .then(parts => {
            // ✅ Show parts display table
            document.getElementById('parts-display').style.display = 'block';

            // ✅ Hide the modal
            closeModal('search-form');

            const allPartsList = document.getElementById('all-parts-list');
            allPartsList.innerHTML = '';

            // ✅ Combine both common and variant parts into one array
            const combinedParts = [...parts.common_parts, ...parts.variant_parts];

            combinedParts.forEach(part => {
                allPartsList.innerHTML += `
                    <tr>
                        <td>${part.part_no}</td>
                        <td>${part.name}</td>
                        <td>${part.material}</td>
                        <td>${part.technical_details}</td>
                        <td>${part.drawing_file ? `<a href="${part.drawing_file}" download>Download</a>` : 'N/A'}</td>
                        <td>${part.cad_file ? `<a href="${part.cad_file}" download>Download</a>` : 'N/A'}</td>
                        <td>${part.mapping ? `<a href="${part.mapping}" download>Download</a>` : 'N/A'}</td>
                    </tr>`;
            });
        })
        .catch(error => {
            console.error('Error fetching parts:', error);
            alert('Failed to load parts data.');
        });
}
