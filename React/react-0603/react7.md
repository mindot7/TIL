## 7.0 To Do List part.1

```js
// App.js

import { useState } from "react"

function App() {
  const [toDo, setToDo] = useState("")
  const [toDos, setToDos] = useState([])
  const onChange = (event) => setToDo(event.target.value)
  const onSubmit = (event) => {
    event.preventDefault()
    if(toDo === ""){
      return
    }
    setToDos((currentArray) => [toDo, ...currentArray])
    setToDo("")
  }
  return (
    <div>
      <h1>My To Dos ({toDos.length})</h1>
      <form onSubmit={onSubmit}>
        <input
          onChange = {onChange}
          value={toDo}
          type="text"
          placeholder="Write your to do..."
        />
        <button>Add To Do</button>
      </form>
    </div>
  )
}

export default App
```







## 7.1 To Do List part.2

- 함수를 보내는 방법

  - `setToDos((currentArray) => [toDo, ...currentArray])`

    - 함수의 첫번째 argument를 현재 state로 보낸다 --> 현재 state를 계산하거나 새로운 state를 만들 수 있다
    - 현재 toDos를 받아와서 새로운 toDo의 array로 return




- map 함수

  - 예전 array를 가져와서 변형한다

  `['there', 'are', 'you', 'are', 'how', 'hello!'].map((item) => item.toUpperCase`

  --> `['THERE', 'ARE', 'YOU', 'ARE', 'HOW', 'HELLO!']`

  

  



