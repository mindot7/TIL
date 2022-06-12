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

