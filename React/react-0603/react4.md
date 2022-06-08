## 4.0 Props

```html
// component
    function Btn({ text, big }) {
      console.log(text, big)
      return (
        <button
          style = {{
            backgroundColor: "tomato",
            color: "white",
            padding: "10px 20px",
            border: 0,
            borderRadius: 10,
            fontSize: big ? 18 : 16  # big이면 18, 아니면 16
		</button>
          }}
        >{text}
        </button>
      )
    }
    // JSX
    function App() {
      return (
        <div>
          <Btn text = "Save Changes" big={true} />
          <Btn text = "Continue" />
        </div>)
      }  
      const root = document.getElementById("root")
    ReactDOM.render(<App />, root)
```



## 4.1 Memo

```html
// component
    function Btn({ text, changeValue }) {
      return (
        <button
        // button은 changevalue라는 onClick 리스너를 가진다
          onClick = {changeValue}
          style = {{
            backgroundColor: "tomato",
            color: "white",
            padding: "10px 20px",
            border: 0,
            borderRadius: 10,
            fontSize: 16,
          }}
        >{text}
        </button>
      )
    }
    // JSX
    function App() {
      const [value, setValue] = React.useState("Save Changes")
      const changeValue = () => setValue("Revert Changes")
      // 이때의 onClick은 이벤트리스너가 아닌 prop
      return (
        <div>
          <Btn text = {value} changeValue = {changeValue} />
          <Btn text = "Continue" />
        </div>)
      }  
      const root = document.getElementById("root")
    ReactDOM.render(<App />, root)
```



#### Memo

```html
const MemorizedBtn = React.memo(Btn)
...
 return (
        <div>
          <MemorizedBtn text = {value} changeValue = {changeValue} />
          <MemorizedBtn text = "Continue" />
        </div>)
```







## 4.2 Prop Types

```html
```

