# 출출
# 0212 // 1315 - 1438 // 1차 실패 : 풀 수 있을 것 같아서 나중에 다시 풀 예정

import sys
sys.stdin = open('a.txt')

# N 개의 문제들 중 M 개를 맞추었다.
# 연속으로 맞추면 점수를 더 많이 준다.
# 카운터가 K 가 되면 해당 문제에 대해 1점 더하고 카운터가 0이 되면서 전체 점수 2배
# 최대 점수

# 일단 K 는 맞추는게 기본이고 그 전까지 최대한 점수를 쌓아야겠네
# 그 뒤로는 그냥 최대한 연속으로 맞추는게 최선인듯?

TC = int(input())
for test_case in range(1, TC+1):
    N, M, K = map(int, input().split())

    X = N - M

    lst = list(range(0, N, K))
    print(lst)

    if N - M >= len(lst):
        score = M
    else:
        for _ in range(K - (N - M)):
            lst.pop()

    count = 0
    score = 0
    for i in range(1, M+1):
        count += 1
        score += 1
        if count in lst:
            score *= 2

    
    print(f'#{test_case} {score}')