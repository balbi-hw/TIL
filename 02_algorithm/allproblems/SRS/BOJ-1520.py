# BOJ - 1520 내리막길

"""
(0, 0) 에서 시작해 (N-1, N-1) 까지 이동

항상 낮은 곳으로만
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
dist = [[-1] * M for _ in range(N)]

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def find_road(r, c) -> None:

    if (r, c) == (N-1, M-1):
        return 1
    
    if dist[r][c] != -1:
        return dist[r][c]
    
    dist[r][c] = 0

    for dr, dc in dirs:
        nr, nc = r+dr, c+dc

        if not (0 <= nr < N and 0 <= nc < M):
            continue

        if field[nr][nc] >= field[r][c]:
            continue

        dist[r][c] += find_road(nr, nc)
    
    return dist[r][c]


print(find_road(0, 0))