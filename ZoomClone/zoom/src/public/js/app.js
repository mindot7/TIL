const messageList = document.querySelector("ul")
const messageForm = document.querySelector("form")
const socket = new WebSocket(`ws://${window.location.host}`)

socket.addEventListener("open", () => {
    console.log("Connected to Server 👍")
})

socket.addEventListener("message", (message) => {
    console.log("New message: ", message.data, " from the server")
})

socket.addEventListener("message", async(event) => {
    console.log(await event.data.text())
})

socket.addEventListener("close", () => {
    console.log("Disconnected from Server 😢")
})


function handleSubmit(event){
    event.preventDefault()
    const input = messageForm.querySelector("input")
    // 프론트에서 백으로 보내주기
    socket.send(input.value)
    // 입력이 끝나면 비워주기
    input.value = ""
}

async function handleMessage(event) {
    const message = await event.data.text()
    console.log(message)
}

messageForm.addEventListener("submit", handleSubmit)