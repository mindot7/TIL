def solution(N, stages):
    answer = []
    players = len(stages)

    for i in range(1, N + 1):
        # fail: 플레이어들이 멈춰있는 스테이지
        fail = stages.count(i)
        # 구글링한 부분, 테스트케이스중 stages가 비어있는 케이스 대비
        if players == 0:
            failure = 0
        # 실패율 = 클리어못한 플레이어 수 / 스테이지에 도달한 플레이어의 수
        else:
            failure = fail / players

        # 전 단계에서 멈춰있는 플레이어 수 빼주기
        players -= fail
        # answer에 (단계, 실패율) append
        answer.append((i, failure))

    # lambda 이용해 실패율의 내림차순
    answer = sorted(answer, key=lambda x: x[1], reverse=True)
    # 스테이지만 출력하기
    answer = [i[0] for i in answer]
    return answer