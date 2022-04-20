n = list(map(int, input()))
left = 0
right = 0
mid = len(n)//2

for i in range(mid):
    left += n[i]

for j in range(mid, len(n)):
    right += n[j]

if left == right:
    print('LUCKY')
else:
    print('READY')