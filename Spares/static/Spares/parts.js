let step = 0;
let partDetails = { detail:'',  partNo: '',  partName: '' };
let chatBox = document.getElementById("chat-box");

function askQuestion() {
    let questions = [
       
         "Do you want to specific details:",
          "Please enter the Part No:",
        "Please enter the Part Name:"
    ];
    
    if (step < questions.length) {
        chatBox.innerHTML += `<div class="chat-message chatbot-message">
                                    <img src="/image/chatbot.jpeg" alt="Chatbot" class="chat-avatar">
                                    <strong>Chatbot:</strong> ${questions[step]}
                              </div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}

function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    if (userInput.trim() === "") return;

    chatBox.innerHTML += `<div class="chat-message user-message">
                                <strong>You:</strong> ${userInput}
                          </div>`;

    if (step === 0) partDetails.detail = userInput;
   
    else if (step === 1) partDetails.partNo = userInput;
    else if (step === 2) partDetails.partName = userInput;

    step++;
    
    setTimeout(() => {
        if (step < 3) {
            askQuestion();
        } else {
            chatBox.innerHTML += `<div class="chat-message chatbot-message">
                                     <img src="/image/chatbot.jpeg" alt="Chatbot" class="chat-avatar">
                                     <strong>Chatbot:</strong> Thank you! Here is your entry:
                                    <br>Details: ${partDetails.detail}

                                     <br>Part No: ${partDetails.partNo}
                                     <br>Part Name: ${partDetails.partName}
                                  </div>`;
        }
        chatBox.scrollTop = chatBox.scrollHeight;
    }, 500);
    
    document.getElementById("user-input").value = "";
}

// Initialize chat with first question
setTimeout(askQuestion, 500);