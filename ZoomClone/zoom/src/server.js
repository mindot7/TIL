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

const handleListen = () => console.log(`Listening on http://localhost:3000`)
app.listen(3000, handleListen)