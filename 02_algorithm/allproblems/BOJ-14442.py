# BOJ - 14442 | 벽 부수고 이동하기 2
# https://www.acmicpc.net/problem/14442


import sys
from collections import deque

input = sys.stdin.readline


dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]


def make_route(sr, sc, er, ec):

    queue = deque([(sr, sc, K)])
    dist = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
    dist[sr][sc][K] = 1

    while queue:
        r, c, b = queue.popleft()

        if (r, c) == (er, ec):
            print(dist[r][c][b])
            return

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < N and 0 <= nc < M):
                continue

            if field[nr][nc] == 1:
                if b > 0 and dist[nr][nc][b - 1] == 0:
                    dist[nr][nc][b-1] = dist[r][c][b] + 1
                    queue.append([nr, nc, b - 1])

            else:
                if dist[nr][nc][b] == 0:
                    dist[nr][nc][b] = dist[r][c][b] + 1
                    queue.append([nr, nc, b])

    print(-1)


N, M, K = map(int, input().split())
field = [list(map(int, list(input().strip()))) for _ in range(N)]

make_route(0, 0, N-1, M-1)