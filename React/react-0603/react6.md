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







## 6.2 Deps

### search bar를 만들어보자

`const [keyword, setKeyword] = useState("")`

- first item: value

- second item: value를 modify하는 function

  

### 특정한 부분만이 변화했을 때, 원하는 코드들을 실행할 수 있는 방법을 배우고 싶어!

` useEffect(() => {console.log("SEARCH FOR", keyword)}, [keyword])`

- 'keyword'가 변화할 때 코드를 실행할 거라고 react.js에게 알려준다

` useEffect(() => {if (keyword !== "" && keyword.length > 5) {console.log("SEARCH FOR", keyword)}}, [keyword])`

- 'keyword'가 비어있지 않고 keyword의 길이가 5보다 길 때 검색을 하겠다



## 6.3 Recap

### useEffect

1. argument
   1. 우리가 실행시키고 싶은 코드
   2. dependencies: react.js가 지켜보아야 하는 것들

2. 우리가 언제 코드를 실행시킬지 선택할 수 있다







## 6.4 Cleanup

```js
function hiFn() {
    console.log("created :)")
    return byeFn
  }
```

- component가 파괴될 때는 react.js는 hiFn이 return한 function을 실행한다

```js
// App.js

import { useState, useEffect } from "react"

function Hello() {
  function byeFn() {
    console.log("bye :(")
  }
  function hiFn() {
    console.log("created :)")
    return byeFn
  }
  useEffect(hiFn, [])
  return <h1>Hello</h1>
}

function App() {
  const [showing, setShowing] = useState(false)
  const onClick = () => setShowing((prev) => !prev)
  return (
   <div>
    {showing ? <Hello /> : null}
    <button onClick={onClick}>{showing ? "Hide": "Show"}</button>
  </div>
  )
}

export default App;
```

