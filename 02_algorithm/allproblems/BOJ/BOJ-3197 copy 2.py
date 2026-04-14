# BOJ - 3197 | 백조의 호수
# https://www.acmicpc.net/problem/3197


import sys
from collections import deque

input = sys.stdin.readline

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

R, C = map(int, input().split())
lake = []
swans = []

water_q = deque()

for r in range(R):
    row = list(input().strip())
    for c in range(C):
        if row[c] != 'X':          # 물(.)과 백조(L)는 모두 물 취급
            water_q.append((r, c))
        if row[c] == 'L':
            swans.append((r, c))
    lake.append(row)

(sr, sc), (er, ec) = swans

# 백조 이동용 큐
swan_q = deque([(sr, sc)])
next_swan_q = deque()
swan_visited = [[False] * C for _ in range(R)]
swan_visited[sr][sc] = True


def move_swan() -> bool:
    while swan_q:
        r, c = swan_q.popleft()

        if (r, c) == (er, ec):
            return True

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if swan_visited[nr][nc]:
                continue

            swan_visited[nr][nc] = True

            if lake[nr][nc] == 'X':
                next_swan_q.append((nr, nc))   # 오늘은 못 감, 내일 시도
            else:
                swan_q.append((nr, nc))        # 오늘 바로 이동 가능

    return False


def melt():
    water_size = len(water_q)

    for _ in range(water_size):
        r, c = water_q.popleft()

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < R and 0 <= nc < C):
                continue

            if lake[nr][nc] == 'X':
                lake[nr][nc] = '.'
                water_q.append((nr, nc))


days = 0

while True:
    if move_swan():
        print(days)
        break

    melt()
    swan_q = next_swan_q
    next_swan_q = deque()
    days += 1