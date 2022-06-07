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

