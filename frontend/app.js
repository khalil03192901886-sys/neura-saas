const API = "http://127.0.0.1:8000";

// REGISTER
function register(){
    let username = document.getElementById("user").value;
    let password = document.getElementById("pass").value;

    fetch(API + "/register", {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body: JSON.stringify({username,password})
    })
    .then(r=>r.json())
    .then(d=>{
        alert("Registered!");
        window.location="login.html";
    });
}

// LOGIN
function login(){
    let username = document.getElementById("user").value;
    let password = document.getElementById("pass").value;

    fetch(API + "/login", {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body: JSON.stringify({username,password})
    })
    .then(r=>r.json())
    .then(d=>{
        if(d.token){
            localStorage.setItem("user", username);
            window.location="index.html";
        }else{
            alert("Login failed");
        }
    });
}

// CHAT
function send(){
    let msg = document.getElementById("msg").value;
    let user = localStorage.getItem("user");

    fetch(API + "/chat", {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body: JSON.stringify({username:user, message:msg})
    })
    .then(r=>r.json())
    .then(d=>{
        document.getElementById("chat").innerHTML +=
        `<div class="msg">You: ${d.user}</div>
         <div class="msg">AI: ${d.ai}</div>`;
    });
}
