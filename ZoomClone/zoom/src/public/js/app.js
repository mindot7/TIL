const socket = io()

// home.pug의 div#welcome을 의미함
const welcome = document.getElementById("welcome")

const form = welcome.querySelector("form")


function handleRoomSubmit(event){
    event.prventDefault()
    const input = form.querySelector("input")
    // socket.emit: 어떤 event든지 전송 할 수 있다
    socket.emit("enter_room", { payload: input.value }, () => {
        console.log("server is done")
    })
    input.value=""
}

form.addEventListener("submit", handleRoomSubmit)