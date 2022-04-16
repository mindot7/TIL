'''
5 8 3
2 4 5 4 6
'''

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
first = nums[n-1]
second = nums[n-2]
ans = 0

while True:
    for i in range(k):
        if m == 0:
            break
        ans += first
        m -= 1
    if m == 0:
        break
    ans += second
    m -= 1
print(ans)