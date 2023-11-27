function addLeftMessage(message) {
  const chatBody = document.getElementById("chat-body"),
    leftMessage = document.createElement("div"),
    icon = document.createElement("img"),
    span = document.createElement("span");

  leftMessage.className = "left-message";
  icon.className = "icon";
  icon.alt = "icon";
  icon.src = "imgs/bot-icon.png";
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
  icon.src = "imgs/user-icon.png";
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
    url: '/get_message',
    method : 'POST',
    data: {
        message : chatInputContent
    },
    success: function(response){
        console.log(response);
    },
    error: function(xhr, status, error){
        console.log(error);
    }
  });
}
