# BOJ - 1388
# 바닥 장식
# 구현, 그래프

from collections import deque

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]


def bfs(r, c):
    global N, M

    q = deque([(r, c)])
    visited = [[False]*M for _ in range(N)]
    visited[r][c] == True
    count = 0

    while q:
        pr, pc = q.popleft()

        for dr, dc in dirs:
            nr, nc = pr+dr, pc+dc

            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] == False:
                    if field[nr][nc] == field[r][c]:
                        q.append(nr, nc)
                        visited[nr][nc] == True
                    else:
                        count += 1
        

    pass

N, M = map(int, input())
field = [input() for _ in range(N)]

