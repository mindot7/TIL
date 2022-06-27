n = int(input())
A = list(map(int, input().split()))
a, b, c, d = map(int, input().split())
mmax = -1000000000
mmin = 1000000000

def cal(cnt, result, plus, minus, multi, div):
    global mmax
    global mmin
    if cnt == n:  # 백트래킹
        mmax = max(mmax, result)
        mmin = min(mmin, result)
        return
    if plus:  # result에 바뀐 변화값 넣어주기, 쓴 연산은 -1
        cal(cnt + 1, result + A[cnt], plus-1, minus, multi, div)
    if minus:
        cal(cnt + 1, result - A[cnt], plus, minus - 1, multi, div)
    if multi:
        cal(cnt + 1, result * A[cnt], plus, minus, multi - 1, div)
    if div:
        cal(cnt + 1, -(-result // A[cnt]) if result < 0 else result // A[cnt], plus, minus, multi, div -1)

cal(1, A[0], a, b, c, d)
print(mmax)
print(mmin)