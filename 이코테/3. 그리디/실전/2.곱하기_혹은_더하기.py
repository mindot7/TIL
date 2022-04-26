nums = input()
result = int(nums[0])  # result에 첫 번째 숫자 대입

for i in range(1, len(nums)):
    num = int(nums[i])
    if num <= 1 or result <= 1:  # 두 수 중에 하나라도 0 이나 1이 있을 경우 -> 더하기
        result += num
    else:  # 곱하기
        result *= num
print(result)

'''
02984

576


567

210
'''