# SWEA - 1486
# 장훈이의 높은 선반

from itertools import combinations

def dfs(idx, h):
    global B, lst, min_h

    # 기저조건
    # 끝까지 다 돌아봤을 때
    # 높이가 조건을 만족하면 최솟값 갱신
    # if h >= B or idx == N:
    if idx == N:
        if h >= B:
            min_h = min(min_h, h)
        return 
    
    # 가지치기
    # 싹수가 노란 놈들은 미리 자른다.
    if h >= min_h:
        return
    
    # 함수 내용
    # 지금 인덱스의 키를 더하거나 건너뛰거나니까
    # 더하거나
    dfs(idx+1, h+lst[idx])
    # 건너뛰거나
    dfs(idx+1, h)

    pass

TC = int(input())
for test_case in range(1, TC+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))

    # 조합?
    # dfs?
    
    # [1] 조합
    cand = []  # 조건을 만족하는 후보군 리스트
    # 1개 조합부터 N개 조합까지
    for i in range(1, N+1):  
        nlst = combinations(lst, i)  # 조합 생성
    # combinations 의 반환값을 고려한 for문 구성
        for pick in nlst:  
            if sum(pick) >= B:  # 조건 만족 시
                cand.append(sum(pick))  # 후보 등록!
    # 조건을 만족하는 녀석들 중 가장 작은 값을 출력
    print(f"#{test_case} {min(cand)-B}") 

    # [2] dfs
    min_h = float('inf')  # 최소값 변수 생성
    dfs(0, 0)  # 함수로 DIVE
    # 날출 힘력
    print(f'#{test_case} {min_h - B}')
