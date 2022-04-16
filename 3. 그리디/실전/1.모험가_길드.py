n = int(input())
advents = list(map(int, input().split()))

advents.sort()

group = 0  # 총 그룹의 수
cnt = 0  # 모험가의 수

for i in advents:
    cnt += 1
    if cnt >= i:  # 모험가의 수 >= 공포도 --> 새로운 그룹 만들기
        group += 1
        cnt = 0
print(group)

'''
5
2 3 1 2 2

2
'''