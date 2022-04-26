n = list(map(int, input()))
left = 0
right = 0
mid = len(n)//2

for i in range(mid):  # 1번부터  (mid-1)번 인덱스까지
    left += n[i]

for j in range(mid, len(n)):  # (mid)번 인덱스부터 마지막 인덱스까지
    right += n[j]

if left == right:
    print('LUCKY')
else:
    print('READY')