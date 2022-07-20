## 5.0 Introduction

### node.js 설치

nodejs.org에서 LTS다운로드

커맨드 창에서

```bash
node -v
v.16.15.0
```

```bash
npm 도 확인!
```

```bash
npx create-react-app 폴더명
```



설치 완료되면 'package.json' 확인

```bash
npm start
```

자동으로 개발용 서버(브라우저)가 열리게 됨

- react-scripts'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는 배치 파일이 아닙니다.

  `npm install -save read-scripts`



### 폴더

src폴더

- 모든 파일들을 넣을 폴더

index.js

- ReactDOM, document.getElementById 등 이 있다



creat-react-app은 어플리케이션을 가지고 여기 index.html 안에 넣어주도록 설정되어 있음



마우스 우클릭 후 Inspect들어가면 'static/js' 들이 있는데 이는 실제로 index.html에 존재하지 않는다



### create-react-app의 장점

- Auto-Reload(자동 재실행)

  - App.js

    ```js
    function App() {
        return (
        ...
        <p> ~~~ </p>)
    }
    ```

    p 태그안에 내용을 바꿔주고 저장하면 화면의 내용이 바뀜!



### index.js 정리하기

```js
import React from 'react'
import ReactDOM from 'react-dom'
import App from './App'

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
)
```

만 남기고 다 지울것!



### App.js 정리하기

```js
function App() {
  return (
    <div>
      <h1>
        Hi MJ
      </h1>
    </div>
  )
}
export default App;
```



### 폴더 정리

### 삭제 파일 목록

App.css, App.test.js, index.css, logo.svg, reportWebVitals.js, setupTests.js

그냥 App.js와 inde.js 만 남기면 됨!



### 정리

어플리케이션 만들기

npm start

어플리케이션 정리





## 5.1 Tour of CRA

src폴더 안에 Button.js 만들기

```js
function Button({ text }) {
  return <button>{text}</button>
}
export default Button
```

후에 App.js에서 import 해주기

```js
import Button from "./Button"

function App() {
  return (
    <div>
    ...
      <Button />
    </div>
  )
}
```



```bash
npm i prop-types
```

```js
# src.Button.js
import PropTypes from "prop-types"

function Button({ text }) {
  return <button>{text}</button>
}

Button.propTypes = {
  text: PropTypes.string.isRequired,
}
export default Button
```





style.css 만들기

```css
button {
  color:white;
  background-color: tomato
}
```



index.js에서 import 해주기

```js
import "./style.css"
```



Button.js에서 button style 지정해주기 (필요없는듯??)

```js
function Button(
	return(
    <button 
    style={{
      backgroundColor: "tomato",
      color: "white",
  }}
  >
    )
)
```



Button.module.css 만들고 내용 적기

```css
.btn {
  color: white;
  background-color: tomato;
}
```



Button.js에서 

```js
function Button({ text }) {
  return (
  <button 
    className = {styles.btn}>{text}</button>
  )
}
```



이후 페이지에서 Elements를 확인하면

```html
<button class="Button_btn__-f8Nl">Continue</button>
```

creact-react-app은 무작위적인 랜덤 class를 갖는다



App.module.css 만들기

```css
.title {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  font-size: 18px;
}
```



App.js에서 App.module.css import 해주고 h1에 className 설정

```js
import styles from "./App.module.css"

function App() {
    ...
    <h1 className={styles.title}>
}
```

이후 Elements 확인 시 h1에는 className 이 정해져있음

```css
<h1 class="App_title__qa9Yc">Hi MJ</h1>
```


언제하지...
