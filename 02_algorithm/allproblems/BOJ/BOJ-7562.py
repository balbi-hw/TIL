# BOJ - 7562 | 나이트의 이동
# https://www.acmicpc.net/problem/7562


import sys
from collections import deque

input = sys.stdin.readline


DIRS = [
    (-2, 1), (-1, 2), (1, 2), (2, 1),
    (2, -1), (1, -2), (-1, -2), (-2, -1)
]


def move_knight(sr, sc, er, ec):

    queue = deque([(sr, sc)])
    dist = [[None] * N for _ in range(N)]
    dist[sr][sc] = 0

    while queue:
        r, c = queue.popleft()

        if (r, c) == (er, ec):
            print(dist[r][c])
            return 

        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < N and 0 <= nc < N):
                continue

            if dist[nr][nc]:
                continue
            
            dist[nr][nc] = dist[r][c] + 1
            queue.append((nr, nc))


TC = int(input())
for test_case in range(1, TC+1):
    N = int(input().strip())

    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())

    move_knight(sr, sc, er, ec)

    # print(f"#{test_case} {move_knight(sr, sc, er, ec)}")
