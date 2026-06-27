async function sendMessage(){

    const input=document.getElementById("message");

    const chat=document.getElementById("chatBox");

    if(input.value==="") return;

    chat.innerHTML+=`
        <div class="mb-3">
            <b>You:</b>
            ${input.value}
        </div>
    `;

    const res=await fetch("/assistant/chat",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            message:input.value

        })

    });

    const data=await res.json();

    chat.innerHTML+=`
        <div class="mb-4 text-info">
            <b>CommunityHero AI:</b>
            ${data.reply}
        </div>
    `;

    chat.scrollTop=chat.scrollHeight;

    input.value="";

}