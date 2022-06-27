'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''

n, m = map(int, input().split())

teul = []
for _ in range(n):
    teul.append(list(map(int, input())))

def dfs(x, y):
    # 범위 벗어나면 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    # 미방문 좌표일 경우
    if teul[x][y] == 0:
        # 방문 처리
        teul[x][y] = 1
        # 상하좌우 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)