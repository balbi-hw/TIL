# BOJ - 20056  마법사 상어와 파이어볼

import sys
from collections import defaultdict

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


# matrix = []
# for _ in range(N):
matrix = [[[] for _ in range(N)] for _ in range(N)]

info = defaultdict(list)

for _ in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    info[(r, c)] = [m, s, d]
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

for _ in range(K):

    cur_info = list(info)

    for pos in cur_info:

        if not info[pos]:
            continue
        # [1] 이동
        # s = info[][1], d = info[][2]
        r, c = pos
        m, s, d = info[pos]

        # 델타 추출
        dr, dc = dirs[d]
        npos = (r + (dr*s), c + (dc*s))


        # 없으면 이동하고 있으면 일단 추가
        if not info[npos]:
            info[npos].append([m, s, d])
            info[pos] = []
        else:
            info[npos].append([m, s, d])
            info[pos] = []
            # 익스텐드 때리고 range step 으로 병합하자.
        
        # 이러면 info[i % 3] = m, info[(i+1) % 3] = s, info[(i+2) % 3] = d
        # range(0, len(info[npos]), 3)

    # [3] 분리
    cur_info = list(info)

    while all(len(info[pos]) >= 2 for pos in cur_info):
        for pos in cur_info:
            # 3보다 작으면 한 개라는 뜻
            if len(info[pos]) <= 3:
                continue
            
            r, c = pos
            num = len(info[pos]) // 3
            mass = velo = 0
            d = []
            
            for i in range(len(info[pos])):
                m, s, a = info[pos][i]
                mass += m
                velo += s
                d.append(a)
            
            nd_px = all(di%2 == 1 for di in d)

            if nd_px:
                nd = [1, 3, 5, 7]
            else:
                nd = [0, 2, 4, 6]

            for d in nd:
                info[(r, c)].append([mass//5, velo//num, d])
                info[pos] = []

        cur_info = list(info)

        for pos in cur_info:
            if not info[pos]:
                continue
            
            if info[pos][0] == 0:
                info.pop(pos)
    
    print(1)

result = 0
for lst in info.values():
    for b in lst:
        result += b[0]

print(result)