React JS와 ReactDOM 코드 import

```html
<script src="https://unpkg.com/react@17.0.2/umd/react.production.min.js"></script>
<script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.production.min.js"></script>
```

React JS는 element를 생성하고 event listener를 더하는 것을 도와준다 => interactive power

ReactDOM

- React element들을 가져다가 HTMl로 바꾼다
  - body에 비어있는 div 생성
    - ReactDOM이 React element들을 가져다놓을 곳



CreateElement를 안 쓴다!!

JSX: JavaScript를 확장한 문법

- HTML 코드와 유사



브라우저에서 오류가 남

=> Babel을 써야 한다

- JSX로 적은 코드를 브라우저가 이해할 수 있는 형태로 바꿔준다

```html
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
<script type="text/babel">
```
다음 강의에서는 createElement를 생략하는 방법을 배울 것이다
