'''
3 3
3 1 2
4 1 4
2 2 2

2 4
7 3 1 8
3 3 3 4
'''

n, m = map(int, input().split())

result = 0

for _ in range(n):
    cards = list(map(int, input().split()))

    min_value = min(cards)
    result = max(result, min_value)

print(result)