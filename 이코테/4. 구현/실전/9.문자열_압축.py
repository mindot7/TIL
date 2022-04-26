def solution(s):
    answer = 0
    length = []
    strs = ''

    if len(s) == 1:
        return 1

    for part in range(1, len(s) // 2 + 1):  # 중간까지만 검사하기
        cnt = 1
        part_next = s[:part]
        for i in range(part, len(s), part):  # i가 증가함에 따라 자르는 단위를 증가시켜주기
            if s[i:i+part] == part_next:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ''  # 숫자로 묶어줄 게 없다
                strs += str(cnt) + part_next
                part_next = s[i:i+part]  # 다음 검사를 위해 초기화
                cnt = 1

        if cnt == 1:
            cnt = ''
        strs += str(cnt) + part_next
        length.append(len(strs))
        answer = min(length)
        strs = ''  # 다음 검사를 위해 초기화

    return answer