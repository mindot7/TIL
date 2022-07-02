import http from "http"
import WebSocket from "ws"
import express from "express"

const app = express()

// view engine을 pug로 설정
app.set("view engine", "pug")
// views 디렉토리 설정
app.set("views", __dirname + "/views")
// public 폴더를 유저에게 공개해 준다
// /public으로 이동할 시 public 폴더 내용을 볼 수 있다!
app.use("/public", express.static(__dirname + "/public"))
// home으로 가면 request, response를 받고 res.render(home을 render한다)
app.get("/", (req, res) => res.render("home"))
// 어떤 url을 입력하더라도 무조건 home으로 가게 만들어주기
app.get("/*", (req, res) => res.redirect("/"))

// localhost:3000은 http, ws 둘 다 작동시킬 수 있다
const handleListen = () => console.log(`Listening on http://localhost:3000`)

// http 서버
const server = http.createServer(app)

// 웹소켓 서버 (http서버가 있으면, 그 위에서 ws 서버를 만들 수 있다)
const wss = new WebSocket.Server({ server })

const sockets = []

wss.on("connection", (socket) => {
    sockets.push(socket)
    socket["nickname"] = "익명"
    console.log("Connected to Browser 👍")
    socket.on("close", () => console.log("Disconnected from Browser 😢"))
    socket.on("message", (msg) => {
        // 이게 없으면 ul 에 [object blob]으로 뜬다
        msg = msg.toString('utf-8')
        const message = JSON.parse(msg)
        switch(message.type){
            case "new_message":
                sockets.forEach((aSocket) => aSocket.send(`${socket.nickname}: ${message.payload}`))
            case "nickname":
                socket["nickname"] = message.payload
        }
        // console.log(parsed, message)
    })
})

server.listen(3000, handleListen)