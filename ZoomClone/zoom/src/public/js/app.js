const messageList = document.querySelector("ul")
const nickForm = document.querySelector("#nick")
const messageForm = document.querySelector("#message")
const socket = new WebSocket(`ws://${window.location.host}`)

function makeMessage(type, payload) {
    const msg = {type, payload}
    return JSON.stringify(msg)
}

socket.addEventListener("open", () => {
    console.log("Connected to Server 👍")
})

// socket.addEventListener("message", (message) => {
//     console.log("New message: ", message.data, " from the server")
// })

// socket.addEventListener("message", async(event) => {
//     console.log(await event.data.text())
// })

socket.addEventListener("message", (message) => {
    const li = document.createElement("li")
    li.innerText = message.data
    // li를 messageList 안에 넣어주기
    messageList.append(li)
})

socket.addEventListener("close", () => {
    console.log("Disconnected from Server 😢")
})


function handleSubmit(event){
    event.preventDefault()
    const input = messageForm.querySelector("input")
    // 프론트에서 백으로 보내주기
    socket.send(makeMessage("new_message", input.value))
    // 입력이 끝나면 비워주기
    input.value = ""
}

async function handleMessage(event) {
    const message = await event.data.text()
    console.log(message)
}

// function handleSubmit(event){
//     event.preventDefault()
//     const input = messageForm.querySelector("input")
//     socket.send(input.value)
//     input.value= ""
// }

function handleNickSubmit(event){
    event.preventDefault()
    const input = nickForm.querySelector("input")
    socket.send(makeMessage("nickname", input.value))
}

messageForm.addEventListener("submit", handleSubmit)
nickForm.addEventListener("submit", handleNickSubmit)