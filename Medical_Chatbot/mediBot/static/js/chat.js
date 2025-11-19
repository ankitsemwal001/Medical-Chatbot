function loadMessages() {
    fetch("/fetch/")
        .then(res => res.json())
        .then(data => {
            const chat = document.getElementById("chatBox");
            chat.innerHTML = "";

            data.messages.forEach(m => {
                const div = document.createElement("div");
                div.className = m.sender === "user" ? "msg right" : "msg left";
                div.innerHTML = `<p>${m.message}</p>`;
                chat.appendChild(div);
            });

            chat.scrollTop = chat.scrollHeight;
        });
}

setInterval(loadMessages, 1000);
loadMessages();

function sendMessage() {
    const text = document.getElementById("userInput").value;
    if (!text.trim()) return;

    const formData = new FormData();
    formData.append("message", text);

    fetch("/send/", {
        method: "POST",
        body: formData,
        headers: { "X-CSRFToken": getCsrfToken() }
    })
    .then(res => res.json())
    .then(() => {
        document.getElementById("userInput").value = "";
        loadMessages();
    });
}

function getCsrfToken() {
    let cookieValue = null;
    document.cookie.split(";").forEach(cookie => {
        cookie = cookie.trim();
        if (cookie.startsWith("csrftoken=")) {
            cookieValue = cookie.slice("csrftoken=".length);
        }
    });
    return cookieValue;
}
