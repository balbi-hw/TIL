# BOJ - 17779  게리맨더링 2

# 5구역을 정하는 문제
# 5구역 스타트는 가장자리는 안된다.
# 보니까 5구역은 마름모 모양이어야만 하는 것 같고
# 바람개비 모양이네
# 12시: 1, 3시: 2, 6시: 4, 9시: 3
# 맨해튼 거리? 랑은 조금 다른가
# 디저트 카페?
# 가생이 안되고 양옆 안되고 맨 아래 두 칸도 안된다.

import sys

dirs = [
    (1, 1), (1, -1), (-1, -1), (-1, 1)
]

def cal(edge: list, visited: list):
    global field, min_dif

    checked = [[False]*N for _ in range(N)]
    up, down, left, right = edge

    up_r, up_c = up
    down_r, down_c = down
    left_r, left_c = left
    right_r, righr_c = right

    # one
    one = 0
    two = 0
    thr = 0
    fou = 0
    fiv = 0
    
    edge = [(0, 1), (5, 4), (1, 0), (4, 5)]

    for r in range(left_r):
        for c in range(up_c + 1):
            if visited[r][c]:
                break
            checked[r][c] = True
            one += field[r][c]

    for r in range(right_r + 1):
        for c in range(N-1, up_c, -1):
            if visited[r][c]:
                break
            checked[r][c] = True
            two += field[r][c]

    for r in range(left_r, N):
        for c in range(down_c):
            if visited[r][c]:
                break
            checked[r][c] = True
            thr += field[r][c]

    for r in range(right_r + 1, N):
        for c in range(N-1, down_c-1, -1):
            if visited[r][c]:
                break
            checked[r][c] = True
            fou += field[r][c]

    for r in range(N):
        for c in range(N):
            if not checked[r][c]:
                fiv += field[r][c]

    highest = max(one, two, thr, fou, fiv)            
    lowest = min(one, two, thr, fou, fiv)

    min_dif = min(min_dif, highest - lowest)
    if min_dif == 100:
        print(thr, two)

    if edge == [(0, 1), (5, 4), (1, 0), (4, 5)]:
        sys.exit(0)


def find_edges(visited: list):
    edge = []
    # 상단
    for i in range(N):
        if True in visited[i]:
            edge.append((i, visited[i].index(True)))
            break
    # 하단
    for i in range(N-1, -1, -1):
        if True in visited[i]:
            edge.append((i, visited[i].index(True)))
            break
    # 좌단
    for r in range(N):
        if len(edge) == 3:
            break
        for c in range(N):
            if visited[c][r] == True:
                edge.append((c, r))
                break
    # 우단
    for i in range(N-1, -1, -1):
        if len(edge) == 4:
            break
        for j in range(N-1, -1, -1):
            if visited[j][i] == True:
                edge.append((j, i))
                break
    
    return edge


def dfs(r: int, c: int, d: int, count: int):
    # 방향 인덱스 3, 원래 위치
    global pos, visited

    cand = (d,) if count == 1 else (d, d+1)

    for nd in cand:
        if nd >= 4:
            continue
        
        dr, dc = dirs[nd]
        nr, nc = r+dr, c+dc

        if not (0 <= nr < N and 0 <= nc < N):
            continue

        if (nr, nc) == pos:
            if nd == 3 and count >= 4:
                edge = find_edges(visited)
                cal(edge, visited)
            continue

        if visited[nr][nc]:
            continue

        visited[nr][nc] = True
        dfs(nr, nc, nd, count + 1)
        visited[nr][nc] = False
        

N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]


min_dif = float('inf')

for r in range(N-2):
    for c in range(1, N-1):
        visited = [[False] * N for _ in range(N)]
        pos = (r, c)
        visited[r][c] = True
        dfs(r, c, 0, 1)


print(min_dif)