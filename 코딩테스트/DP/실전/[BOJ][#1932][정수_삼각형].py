n = int(input())
t = []
for i in range(n):
    t.append(list(map(int, input().split())))
m = 2
for i in range(1, n):
    for j in range(m):
        if j == 0:  # 제일 왼쪽
            t[i][j] = t[i][j] + t[i-1][j]
        elif i == j:  # 제일 오른쪽
            t[i][j] = t[i][j] + t[i-1][j-1]
        else:
            t[i][j] = max(t[i-1][j-1], t[i-1][j]) + t[i][j]
    m += 1  # 세번째줄~마지막줄
print(max(t[n-1]))