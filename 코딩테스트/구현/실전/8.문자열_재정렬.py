'''
K1KA5CB7

ABCKK13


AJKDLSI412K4JSJ9D

ADDIJJJKKLSS20
'''

sstr = input()
ans = []
num = 0

for i in sstr:
    if i.isalpha():  # 문자면,
        ans.append(i)  # 리스트에 넣기
    else:  # 숫자면,
        num += int(i)  # num에 합해주기

ans.sort()  # 문자순 배열
ans.append(str(num))  # 그냥 num 넣으면 print 쪽에서 "TypeError: sequence item 5: expected str instance, int found" 나옴

print(''.join(ans))  # 따옴표 없애고 한번에 출력