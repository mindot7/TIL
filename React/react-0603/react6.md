## 6.0 Introduction

```js
// App.js

import { useState } from "react"

function App() {
  const [counter, setValue] = useState(0)
  const onClick = () => setValue((prev) => prev + 1)
  console.log('render')
  return (
    <div>
      <h1>{counter}</h1>
      <button onClick={onClick}>Click Me</button>
    </div>
  )
}

export default App;
```

- 처음에 `npm  start`로 브라우저를 열려고 시도했는데 

  *react-scripts'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는 배치 파일이 아닙니다.*

  라는 에러 메시지가 떴다

  - ``npm install -save read-scripts`로 해결!





## 6.1 useEffect

### 특정 코드의 실행을 제한하고 싶어! --> component가 맨 처음 render될 때에만!

useEffect

- 두 개의 argument를 가지는 function
  - 첫 번째 argument: 우리가 딱 한 번만 실행하고 싶은 코드
  - 두 번쨰 argument: 나중에...?

```js
// App.js

...
function App() {
  const [counter, setValue] = useState(0)
  const onClick = () => setValue((prev) => prev + 1)
  console.log('i run all the time')
  const iRunOnlyOnce = () => {
    console.log("i run only once.")
  }
  useEffect(iRunOnlyOnce, [])
...

```

- 브라우저에 Click me 버튼을 클릭하면 console 창에 'i run all the time'만 새로 출력된다

