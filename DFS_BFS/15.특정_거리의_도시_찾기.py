from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)
visited[x] = 0

for _ in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)

que = deque([x])

while que:
    c = que.popleft()
    for n in graph[c]:
        if visited[n] == -1:
            visited[n] = visited[c] + 1
            que.append(n)
for i in range(n+1):
    if visited[i] == k:
        print(i)
if k not in visited:
    print(-1)