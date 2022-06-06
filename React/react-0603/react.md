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





## 2. 6  JSX part.2

= () => : arrow function





컴포넌트의 첫 글자는 반드시 대문자여야 한다

```html
const Container = (
      <div>
        <Title /> <Button />
      </div>
    )
```



JSX는 어플리케이션을 여러 가지 작은 요소로 나누어 관리할 수 있게 해준다
다음 강의에서는 createElement를 생략하는 방법을 배울 것이다





## 3.0 Understanding State

state: 데이터가 저장되는 곳



## 3.1  setState part.1

```html
React.useState()
```

--> console창에 [undefined, f] == [초기값, 함수]

```html
const x = [1, 2, 3]
const [a, b, c] = x
```

a는 1, b는 2, c는 3

- JS의 문법



## 3.2 setState part.2

```html
const root = document.getElementById("root")
    function App() {
      const [counter, setCounter] = React.useState(0)
      const onClick = () => {
        setCounter(counter + 1)
      }
      return(
        <div>
          <h3>Total clicks: {counter}</h3>
          <button onClick={onClick}>Click me</button>
        </div>
      )
    }
    ReactDOM.render(<App />, root)
```





## 3.3 Recap

modifier 함수를 가지고 state를 변경할 때 컴포넌트 전체가

새로운 값을 가지고 재생성 된다

컴포넌트란? function App



**state가 바뀌면 리렌더링이 일어난다**





## 3.4 state Functions

함수를 전달하기 (그대로 설정하는 것 대신!)

```html
// setCounter(counter + 1)
        setCounter((current) => current + 1)
```





## 3.5 Input and State

```html
function App() {
      const [minutes, setMinutes] = React.useState()
      const onChange = (event) => {
        setMinutes(event.target.value)
      }
      return(
        <div>
          <h1 className="hi">Super Converter</h1>
          <label htmlFor="minutes">Minutes</label> #'htmlFor'
          <input 
            value = {minutes}
            id="minutes"
            placeholder="Minutes"
            type="number"
            onChange = {onChange}
          />
          <h4>You want to convert {minutes}</h4>
          <label htmlFor="hours">Hours</label>
          <input id="hours" placeholder="Hours" type="number" />
          </div>
        )
    }
    const root = document.getElementById("root")
    ReactDOM.render(<App />, root)
```

