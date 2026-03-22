# BOJ - 21736 헌내기는 친구가 필요해
# https://www.acmicpc.net/problem/21736

import sys
sys.setrecursionlimit(10**7)

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def move(r, c):
    global N, M
    if not (0 <= r < N and 0 <= c < M):
        return False
    if field[r][c] == "X":
        return False
    if visited[r][c]:
        return False
    return True

def find_target(r, c):
    global count

    for dr, dc in dirs:
        nr, nc = r+dr, c+dc

        if move(nr, nc):
            visited[nr][nc] = True
            if field[nr][nc] == "P":
                count += 1
            find_target(nr, nc)
            

N, M = map(int, input().split())
field = []
for r in range(N):
    row = input().strip()
    field.append(row)
    if "I" in row:
        pos = (r, row.index("I"))
visited = [[False] * M for _ in range(N)]

count = 0
r, c = pos
visited[r][c] = True
find_target(r, c)

print(count if count else "TT")