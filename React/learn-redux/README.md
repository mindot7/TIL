## 리덕스에서 사용되는 키워드

### 액션  (Action)

- 상태에 어떤 **변화가 필요할 때**

- `type` 필드는 필수, 그 외에는 상관 X

- ```js
  {
    type: "ADD_TODO",
    data: {
      id: 0,
      text: "리덕스 배우기"
    }
  }
  ```

- ```js
  {
    type: "CHANGE_INPUT",
    text: "안녕하세요"
  }
  ```



### 액션 생성함수 (Action Creator)

- **액션을 만드는 함수**

- 파라미터를 받아와서 액션 객체 형태로 만들어준다

- WHY?

  컴포넌트에서 쉽게 액션을 발생시키기 위해

  - `export` 키워드를 붙여서 다른 파일에서 불러온다



### 리듀서 (Reducer)

- **변화를 일으키는 함수**

- 두 가지 파라미터를 받아온다

  ```js
  function render(state, action) {
      // 상태 업데이트 로직
      return alteredState
  }
  ```

  - `state` `현재의 상태`와 `action` `전달 받은 액션` 을 참고해 **새로운 상태를 만들어서 반환**

  ```js
  function counter(state, action) {
    switch (action.type) {
      case 'INCREASE':
        return state + 1;
      case 'DECREASE':
        return state - 1;
      default:
        return state;
    }
  }
  ```

  - **`default` 시에는 기존 `state`를 그대로 반환해야 한다**





### 스토어 (Store)

- 1 App 1 Store
- 현재의 앱 상태, 리듀서, + a(내장함수)



### 디스패치 (dispatch)

- 스토어의 내장함수 중 하나

- **액션을 발생시키는 것**

  액션을 파라미터로 전달한다 ex)`dispatch(action)`

- dispatch 호출 --> store에서 reducer 함수 실행 --> 새로운 상태 or default



### 구독 (subscribe)

- 스토어의 내장함수 중 하나
- *subscribe 함수에 특정 함수를 전달해주면, 액션이 디스패치 되었을 때 마다 전달해준 함수가 호출된다*(??)
- *react-redux 라는 라이브러리에서 제공하는 `connect` 함수 또는 `useSelector` Hook 을 사용하여 리덕스 스토어의 상태에 구독한다*(???)





## 리덕스의 3가지 규칙

### 1. 1 App 1 Store

- 여러 개의 스토어 사용이 가능하긴 하지만, 권장하지 않음

  특정 *업데이트가 너무 많을 때*, App의 특정 부분을 *완전히 분리*시키게 될 때



### 2. 상태는 읽기전용

- 리액트의 불변성을 유지해야 하는 이유

  : 객체의 변화를 감지 할 때 *shallow equality* 검사를 하기 때문



### 3. 리듀서는 순수한 함수여야 한다

- 순수한 함수?

  - 리듀서는 `state` `현재의 상태`와 `action` `전달 받은 액션`을 파라미터로 받는데,

    `현재의 상태`는 건드리지 않고, 변화가 일어난 `새로운 상태` 객체를 만들어야 한다

  - same parameter, same result

  > new Date(), 랜덤 숫자, 네트워크에 요청 등의 실행 시 마다 다른 결과값은 어떡하나요?
  >
  > 리듀서 함수의 바깥에서 처리해야 한다
  >
  > *리덕스 미들웨어*를 사용한다







## 리덕스 사용 준비

```bash
$ npx create-react-app learn-redux

$ npm add redux
```



```js
// exercise.js

import { createStore } from 'redux'

// createStore는 스토어를 만들어주는 함수
// 리액트 프로젝트에서는 단 하나의 스토어를 만든다


/* 리덕스에서 관리 할 상태 정의 */
const initialState = {
    counter: 0,
    text: '',
    list: []
}


/* 액션 타입 정의(대문자) */
// 액션 타입이 변경될 경우를 대비(유지보수 용이)
const INCREASE = 'INCREASE'
const DECREASE = 'DECREASE'
const CHANGE_TEXT = 'CHANGE_TEXT'
const ADD_TO_LIST = 'ADD_TO_LIST'



/* 액션 생성함수 정의(camelCase) */
function increase() {
    return {
        type: INCREASE // 액션 객체에는 type 값이 필수
    }
}

// 화살표 함수가 더 간단하니 추천!
const decrease = () => ({
    type: DECREASE
})

const changeText = text => ({
    type: CHANGE_TEXT,
    text
})

const addToList = item => ({
    type: ADD_TO_LIST,
    item
})


/* 리듀서 만들기 (!!불변성 꼭 지켜주기!!) */

function reducer(state = initialState, action) {
    switch (action.type) {
        case INCREASE:
            return {
                ...state,
                counter: state.counter + 1
            }
        case DECREASE: 
            return {
                ...state,
                counter: state.counter - 1
            }
        case ADD_TO_LIST:
            return {
                ...state,
                list: state.list.concat(action.item)
            }
        default:
            return state
    }
}


/* 스토어 만들기 */
const store = createStore(reducer)

console.log(store.getState()) // 현재 store 안에 있는 state 조회

// 스토어 안에 있는 state가 바뀔 때 마다 호출되는 listener 함수
const listener = () => {
    const state = store.getState()
    console.log(state)
}

const unsubscribe = store.subscribe(listener)
console.log(unsubscribe)

// 액션 dispatch
store.dispatch(increase())
store.dispatch(decrease())
store.dispatch(changeText('하이하이'))
store.dispatch(addToList({ id: 1, text: '안뇽'}))
```

