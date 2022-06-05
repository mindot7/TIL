s = input()
cnt = [0, 0]  # 각각 0과 1 묶음 수
n = s[0]

for i in s[1:]:
    if n != i:  # 같지 않으면
        cnt[int(n)] += 1  # 묶음 수 더해주기
    n = i

print(min(cnt))  # 묶음 수 작은 거 출력

'''
0001100

1
'''