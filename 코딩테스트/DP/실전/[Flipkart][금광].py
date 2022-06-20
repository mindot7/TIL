'''2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2'''

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    golds = (list(map(int, input().split())))
    
    mine = []
    index = m

    for _ in range(len(golds) // m):  # 몫 구해주기
        mine.append(list(golds[index-m : index]))
        index += m  # 