## 리액트는 어쩌다 만들어졌을까?

### 배경 

- dom을 직접 건드리는 작업은 번거롭다 --> 코드가 난잡해지기 쉽다

### React의 발상

- dom을 전부 날려버리고 다시 만들어서 보여주자

### 문제점

- 매번 이렇게 하게되면 다양한 문제가 발생

### 해결

- 메모리에게 가상DOM을 만든다.
- 업데이트가 필요한 부분만 가상DOM으로 수정한다.
- 그 이후 REACT의 알고리즘을 통해 다른 부분을 감지하여 실제 DOM에 패치 시켜준다.





## 작업환경 준비

컴포넌트를 여러 파일로 분리해서 저장

일반 JS가 아닌 JSX라는 문법으로 작성



### Webpack

- 여러가지의 파일을 한개로 결합

### Babel

- 새로운 JS(JSX,,,) 문법들을 사용하기 위해





## 나의 첫번째 리액트 컴포넌트

`import React from 'react'`: 리액트 불러오기

`export default Hello`: Hello라는 컴포넌트 내보내기 

```js
// index.js

ReactDOM.render(<App />, document.getElementById('root'))
```

- `ReactDOM.render`

  - 브라우저에 있는 실제 DOM 내부의 리액트 컴포넌트를 렌더링하겠다

  - `id`가 `root`인 DOM을 선택하고 있다

    - public/index.html

      `<div id="root"></div>`

      - *리액트 컴포넌트가 렌더링 될 때: 렌더링된 결과물이 위 div 내부에 렌더링 되는 것*







## JSX

HTML 같이 생겼지만 실제로는 JavaScript

XML 형태로 코드를 작성하면 babel이 JSX를 JavaScript로 변환해준다



### 규칙 (제대로 된 변환을 위해)

1. 태그는 꼭 닫혀야 한다

   내용이 안 들어간다면?

   - Self Closing 태그: `<Hello />`

     

2. 태그는 꼭 하나의 태그로 감싸야 한다

   - `<div>`로 감싸주기

   - table 관련 태그는 `<div>`로 감싸기엔 애매,,,

     - **Fragment**를 쓰자

       ```js
       return (
           <>
             <Hello />
             <div>안녕히계세요</div>
           </>
         )
       ```

       태그를 이름 없이 작성

       브라우저 상에서도 별도의 엘리먼트로 나타나지 않는다

3. JSX 안에 JS 값 사용하기

   - JSX 내부에 JS 변수를 보여줘야 할 때에는 `{}`으로 감싸야 한다

     ```js
     function App() {
       const name = 'react';
       return (
         <>
           <Hello />
           <div>{name}</div>
         </>
       );
     }
     ```

4. style과 className

   - 객체 형태로 작성
   - camelCase 형태로 네이밍

   ```js
   function App() {
     const name = 'react'
     const style = {
       backgroundColor: 'black',
       color: 'aqua',
       fontSize: 24, // 기본 단위 px
       padding: '1rem' // 다른 단위 사용 시 문자열로 설정
     }
   
     return (
       <>
         <Hello />
         <div style={style}>{name}</div>
       </>
     )
   }
   ```

   - CSS class 설정 할 때

     `className=`으로 설정해야 한다

