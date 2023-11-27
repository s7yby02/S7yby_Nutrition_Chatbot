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