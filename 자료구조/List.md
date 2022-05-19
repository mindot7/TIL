# List

가장 기본적인 **순차적인**(sequential) 자료구조



A = [2, 4, 0, 5]

- (2, 4, 0, 5)는 C언어와 달리, A의 원소에 저장되는 것이 아니라 다른 메모리에 각자 저장됨
  - A[0]은 2가 *저장된 주소*를 가리킨다
  - A[2] = A[2] + 1
  - 0에다 그대로 1을 더하는 것이 아니다
  - 그렇다고 0이 사라지는 것도 아님(어딘가에 존재함)
  - A[2]는 1이 저장된 다른 주소를 가리키게 되는 것!
  - A.append(6): 맨 뒤에 6을 삽입(연산)
    - A[4]는 6이 저장된 주소를 가리킨다
  - A.pop(): 맨 뒤의 값을 지우고 리턴
    - 6이 리턴
  - A.pop(1): A[1]을 삭제(연산)하고 리턴
    - 0, 5가 왼쪽으로 한칸씩 메꾼다
  - A.insert(1, 10): A[1]에 10을 삽입
    - 0, 5가 오른쪽으로 한칸씩 밀려남
  - A.remove(value): A에서 value 값(첫번째로 있는)을 찾아서 제거
    - 제거된 자리는 메꿈
  - A.index(value): A에서 value 값(첫번째로 있는)의 인덱스 반환
  - A.count(value): A에서 value 값의 등장 횟수 계산





용량(capacity) 자동조절

- dynamic array

```python
import sys
A = []
print(sys.getsizeof(A)) # 56bytes
A.append(10)
print(sys.getsizeof(A)) # 88bytes
```

```python
A.append(x):
    if A.n<A.capacity:
        A[n] = x
        A.n = n+1
    else: A.n == A.capacity
        B = A.capacity * 2 크기의 리스트 새로 할당
        for i in range(n):
            B[i] = A[i] # 이때 이사비용 O(n) A의 n개 원소만큼 B로 복사해 옮기기 때문
            # del A
            # A = B
```








## 순차적 자료구조 (Sequential Data Structures)

1. 배열, 리스트

   - index로 임의의 원소를 접근
   - A= [3, 2, -1, 5, 7]
   - 연산자 [] A[2]: -1  # O(1)
   - 삽입(append, insert)
   - 삭제(pop # O(1), remove # O(n))

   

2.  stack, queue, dequeue

   - 제한된 접근(삽입, 삭제)도 허용

   - stack: LIFO(Last In First Out) -> 쌓아올린다 생각하면 될듯
   - queue: FIFO(First In First Out) -> 선입선출
   - dequeue: stack + queue



3. Linked List(연결 리스트)
   - 각각의 값은 값 뿐만 아니라, 다음 값의 주소도 가지고 있다
   - 인덱스로 접근X
