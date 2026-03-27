# BOJ - 20056  마법사 상어와 파이어볼

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
'''
N = 매트릭스 크기
M = 파이어볼 갯수
K = 이동 명령 수
'''

# 방향: 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
dirs = [
    (-1, 0), (-1, 1), (0, 1), (1, 1),
    (1, 0), (1, -1), (0, -1), (-1, -1)
]

info = {}

for _ in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    info[(r, c)] = []
    info[(r, c)].append([m, s, d])
    # m: 질량, s: 속력, d: 방향

    '''
    [1] 이동
    d 방향으로 s 만큼 이동한다.

    [2] 병합
    같은 칸은 하나로 합쳐진다.
    
    [3] 분리
    4개의 파이어볼로 나누어진다.
    m = 합쳐진 파이어볼의 질량 합 / 5
    s = 합쳐진 파이어볼 속력 합 / 파이어볼 수
    d = 파이어볼의 방향이 모두 홀수이거나 짝수면 방향은 +, else x
    '''

for i in range(K):

    next_info = {}
    merged = []
    for pos in info:

        # [1] 이동
        for balls in info[pos]:
            r, c = pos
            m, s, d = balls
            if m == 0:
                continue

            # 델타 추출
            dr, dc = dirs[d]
            (nr, nc) = (r + (dr*s), c + (dc*s))
            nr %= N
            nc %= N

            npos = (nr, nc)
            if npos not in next_info:
                # default Flase == +, True == x
                next_info[npos] = [m, s, d, False, 1]
            else:
                next_info[npos][4] += 1
                next_info[npos][0] += m
                next_info[npos][1] += s
                if next_info[npos][2] % 2 != d % 2:
                    next_info[npos][3] = True
                merged.append((npos))
    

    info.clear()

    # [3] 분리
    '''
    merged 순회, 플래그로 방향 결정 후 분리
    > 한 칸에 여러개가 생긴다.
    '''
    for pos in next_info:
        m, s, d, flag, num = next_info[pos]

        info[pos] = []
        if pos in merged:
            m //= 5
            s //= num
            if flag:
                for d in [1, 3, 5, 7]:
                    info[pos].append([m, s, d])
            else:
                for d in [0, 2, 4, 6]:
                    info[pos].append([m, s, d])
        else:
            info[pos].append([m, s, d])


result = 0
for pos in info:
    for ball in info[pos]:
        result += ball[0]

print(result)