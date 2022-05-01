from collections import deque

n, m = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

lab = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def bfs():
    global ans
    q = deque()
    visited = [[-1] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            # 바이러스 있는 곳 큐에 담기
            if lab[i][j] == 2:
                q.append((i, j))
                visited[i][j] = 0

    # 바이러스 퍼지는 과정
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if lab[nx][ny] == 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = 0
                    q.append([nx, ny])


    # cnt: 안전영역
    cnt = 0
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0 and visited[i][j] == -1:
                cnt += 1
    ans = max(ans, cnt)

# 벽 세우기
def wall(x):
    # 3개 세우면
    if x == 3:
        # bfs 돌리기
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall(x+1)
                lab[i][j] = 0
wall(0)
print(ans)