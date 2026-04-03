"""
1. 비를 안 맞을 수 있으면 안 맞게
2. 가능한 늦게 맞도록
3. 후보가 여러개라면 가장 위, 그래도 같다면 가장 왼쪽

좌상단 점을 기준으로 하고..
모든 칸에 대해 이중 for? 너무 무겁다

step 을 적절히 쓰면 그나마 가볍게 할 수 있을 것 같네

1. 격자에 drop 인풋을 받고 기록한다.
2. step 을 적절히 해서 순회하고 순회하며 정보를 기록 | 리스트로 통일, first_candidate[안맞는 곳], second_candidate[맞는 곳]
3. 안맞는 곳을 찾으면 더 순회할 필요 없다. 좌상단을 출력해야하고 좌상단부터 순회하니까 안맞는 곳 찾으면 바로 종료 및 출력
4. 순회가 끝났을 때 first 가 비어있으면 second 에서 후보를 찾는다.
5. 가장 늦게 맞는 부분을 찾아야함.
    - 안에서 가장 작은 값으로 비교하면 되네

무겁다..?
"""

# https://school.programmers.co.kr/learn/courses/30/lessons/468379?language=python3#

def solution(m, n, h, w, drops):
    answer = []
    
    # ===== #
    
    N, M, H, W = m, n, h, w
    desert = [[False] * M for _ in range(N)]
    for index, rain in enumerate(drops, start=1):
        r, c = rain
        desert[r][c] = index
    
    # ------ #
    
    candidate = []
    
    for r in range(N - H + 1):
        for c in range(M - W + 1):
            checking = []
            flag = False
            for i in range(r, r + H):
                if True in desert[i][j] for j in range(c, c + W):
                    checking.append()
                
                for j in range(c, c + W):
                    if desert[i][j]:
                        flag = True
                        checking.append(desert[i][j])
            
            if not flag:
                answer = [r, c]
                return answer
    
            candidate.append([[r, c], checking])
    
    # ------ #
        
    candidate.sort(key=lambda x: -min(x[1]))
    
    answer = candidate[0][0]
    
    # ====== #
    
    return answer