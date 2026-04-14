# BOJ - 3197 | 백조의 호수
# https://www.acmicpc.net/problem/3197

import sys
from collections import deque

input = sys.stdin.readline

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def is_done(swans: list) -> None:

    r, c = swans[0]
    er, ec = swans[1]
    q = deque()
    q.append((r, c, 0))
    dist = [[INF] * C for _ in range(R)]
    dist[r][c] = 0

    while q:
        r, c, count = q.popleft()

        if (r, c) == (er, ec):
            dist[r][c] = min(dist[r][c], count)
            continue

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < R and 0 <= nc < C):
                continue
            
            if dist[nr][nc] > dist[r][c]:
                if lake[nr][nc] == 'X':
                    dist[nr][nc] = count + 1
                    q.append((nr, nc, count + 1))
                else:
                    dist[nr][nc] = count
                    q.append((nr, nc, count))

    return dist[er][ec]


R, C = map(int, input().split())
lake = []
swans = []
for r in range(R):
    row = input().strip()
    lake.append(list(row))
    if 'L' in row:
        swans.append((r, row.index('L')))

INF = 10**18
result = is_done(swans)

if result % 2:
    result //= 2
    result += 1
else:
    result //= 2

print(result)