# python 시간초과, pypy 통과

n, c = map(int, input().split())

house = []
for _ in range(n):
    h = int(input())
    house.append(h)

house.sort()

start = 1
end = house[-1] - house[0]

ans = 0

while (start <= end):
    mid = (start + end) // 2
    first = house[0]
    cnt = 1

    for i in range(1, len(house)):
        if house[i] >= first + mid:
            cnt += 1
            first = house[i]

    if cnt >= c:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)