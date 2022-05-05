# 큐(Queue)

FIFO(First-In First-Out) 규칙의 **순차적** 자료구조

삽입: enqueue 삭제: dequeue

```python
class Queue:
    def __init__(self):
        self.items = []    # 빈 리스트
        self.front-index = 0
    def enqueue(self, val):
        self.items.append(val)
    def dequeue(self):
        if self.front-index == len(self.items):
            print("Q is empty")
        else:
            x = self.items[front-index]
            self.front-index += 1
            return x
```

