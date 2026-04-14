# BOJ - 3197 | 백조의 호수
# https://www.acmicpc.net/problem/3197

import sys
from collections import deque

input = sys.stdin.readline

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]


def is_done(swans: list) -> bool:

    r, c = swans[0]
    er, ec = swans[1]

    q = deque()
    q.append((r, c))
    visited = [[False] * C for _ in range(R)]
    visited[r][c] = True

    while q:
        r, c = q.popleft()

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < R and 0 <= nc < C):
                continue

            if visited[nr][nc]:
                continue

            if lake[nr][nc] == 'L':
                return True

            if lake[nr][nc] != 'X':
                visited[nr][nc] = True
                q.append((nr, nc))

    return False


def swan_area_check(swans: list) -> set:

    q = deque()
    water = set()

    for swan in swans:
        r, c = swan

        q.append((r, c))
        water.add((r, c))

        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < R and 0 <= nc < C):
                    continue

                if (nr, nc) in water:
                    continue

                if lake[nr][nc] == '.':
                    water.add((nr, nc))
                    q.append((nr, nc))

    return water


def melting(water_area: set) -> set:
    
    melted = set()

    for r, c in water_area:
        for dr, dc in dirs:
            nr, nc = r + dr , c + dc

            if not (0 <= nr < R and 0 <= nc < C):
                continue

            if lake[nr][nc] == 'X':
                lake[nr][nc] = '.'
                melted.add((nr, nc))

    return melted


R, C = map(int, input().split())
lake = []
swans = []
for r in range(R):
    row = input().strip()
    lake.append(list(row))
    if 'L' in row:
        swans.append((r, row.index('L')))


days = 0
water_area = swan_area_check(swans)
while not is_done(swans):
    nxt_area = melting(water_area)

    days += 1
    water_area = nxt_area

print(days)