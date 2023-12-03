$(document).ready(function(){
  const chatInput = document.getElementById("chat-input");
  chatInput.addEventListener('keypress', evt=>{
      if(evt.key === "Enter") {
          sendMessage();
      };
  });
  
  const chatSubmit = document.getElementById("chat-submit");
  chatSubmit.addEventListener("click", ()=>{
      sendMessage();
  });
})



function addLeftMessage(message) {
  const chatBody = document.getElementById("chat-body"),
    leftMessage = document.createElement("div"),
    icon = document.createElement("img"),
    span = document.createElement("span");

  leftMessage.className = "left-message";
  icon.className = "icon";
  icon.alt = "icon";
  icon.src = "assets/img/chatbot/bot-icon.png";
  span.textContent = message;

  leftMessage.appendChild(icon);
  leftMessage.appendChild(span);
  chatBody.appendChild(leftMessage);
}

function addRightMessage(message) {
  const chatBody = document.getElementById("chat-body"),
    rightMessage = document.createElement("div"),
    icon = document.createElement("img"),
    span = document.createElement("span");

  rightMessage.className = "right-message";
  icon.className = "icon";
  icon.alt = "icon";
  icon.src = "assets/img/chatbot/user-icon.png";
  span.textContent = message;

  rightMessage.appendChild(icon);
  rightMessage.appendChild(span);
  chatBody.appendChild(rightMessage);
}

function sendMessage() {
  const chatInput = document.getElementById("chat-input"),
        chatInputContent = chatInput.value;
  if (!chatInputContent) return;

  addRightMessage(chatInputContent);
  chatInput.value = '';

  $.ajax({
    url: "/api/chat",
    method : 'POST',
    contentType: "application/json",
    data: JSON.stringify({
        text : chatInputContent
    }),
    success: function(response){
        addLeftMessage(response);
    },
    error: function(xhr, status, error){
        console.log(error);
    }
  });
}