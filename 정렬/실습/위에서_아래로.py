'''
3
15
27
12
'''
n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')