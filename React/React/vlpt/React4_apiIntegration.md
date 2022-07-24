## 1. API 연동의 기본

### HTTP 응답 상태 코드

| 상태코드 |                                                              |
| :------: | :----------------------------------------------------------: |
|   200    |            클라이언트의 요청을 정상적으로 수행함             |
|   201    | 클라이언트가 어떠한 리소스 생성을 요청, 해당 리소스가 성공적으로 생성됨(POST를 통한 리소스 생성 작업 시) |

| 상태코드 |                                                              |
| -------- | ------------------------------------------------------------ |
| 400      | 클라이언트의 요청이 부적절 할 경우 사용하는 응답 코드        |
| 401      | 클라이언트가 인증되지 않은 상태에서 보호된 리소스를 요청했을 때 사용하는 응답 코드 |
|          | (로그인 하지 않은 유저가 로그인 했을 때, 요청 가능한 리소스를 요청했을 때) |
| 403      | 유저 인증상태와 관계 없이 응답하고 싶지 않은 리소스를 클라이언트가 요청했을 때 사용하는 응답 코드 |
|          | (403보다는 400이나 404를 사용할 것을 원고, 403 자체가 리소스가 존재한다는 뜻이기 때문에) |
| 405      | 클라이언트가 요청한 리소스에서는 사용 불가능한 Method를 이용했을 경우 사용하는 응답 코드 |

| 상태코드 |                                                              |
| -------- | ------------------------------------------------------------ |
| 301      | 클라이언트가 요청한 리소스에 대한 URI가 변경 됐을 때 사용하는 응답 코드 |
|          | (응답 시 Locatino header에 변경된 URI를 적어줘야 합니다)     |
| 500      | 서버에 문제가 있을 경우 사용하는 응답 코드                   |



### REST API 메서드

- GET: 데이터 조회
- POST: 데이터 등록
- PUT: 데이터 수정
- DELETE: 데이터 제거
- PATCH
- HEAD



### useState와 useEffect로 데이터 로딩하기

`useState`: 요청 상태 관리

`useEffect`: 컴포넌트가 렌더링되는 시점에 요청 시작

- 3가지 상태 관리
  1. 요청의 결과
  2. 로딩 상태
  3. 에러



```js
// src/Users.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Users() {
  const [users, setUsers] = useState(null);
  const [loading, setLoading]  = useState(false);
  const [error, setError] = useState(null);

  const fetchUsers = async () => {
    try {
      // 요청이 시작 할 때에는 error와 users를 초기화하고
      setError(null);
      setUsers(null);
      // loading 상태를 true로 바꾼다
      setLoading(true);
      const response = await axios.get(
        'https://jsonplaceholder.typicode.com/users'
      );
      setUsers(response.data);
    } catch (e) {
      setError(e);
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  if (loading) return <div>로딩중...</div>;
  if (error) return <div>에러가 발생했습니다</div>
  if (!users) return null;
  return (
    <>
      <ul>
        {users.map(user => (
          <li key={user.id}>
            {user.username} ({user.name})
          </li>
        ))}
      </ul>
      <button onClick={fetchUsers}>다시불러오기</button>
    </>
  );
}

export default Users;
```





## 2. useReducer 로 요청 상태 관리하기

`useReducer`를 사용해 `LOADING`, `SUCCESS`, `ERROR` 액션에 따라 다르게 처리 해보기

`useReducer`의 장점: 재사용





## 3. useAsync 커스텀 Hook 만들어서 사용하기

커스텀 Hook을 만들어서 요청 상태 관리 로직 재사용 방법 알아보기



