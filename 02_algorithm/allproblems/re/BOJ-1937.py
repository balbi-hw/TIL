# BOJ - 1937 | 욕심쟁이 판다

"""
DFS, Memoization
"""

import sys
sys.setrecursionlimit(10**7)

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def dfs(r: int, c: int) -> None:
    global count

    if dp[r][c]:
        return dp[r][c]
    
    dp[r][c] = 1
    
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc

        if not (0 <= nr < N and 0 <= nc < N):
            continue

        if bamboo[nr][nc] <= bamboo[r][c]:
            continue
        
        dp[r][c] = max(dp[r][c], 1 + dfs(nr, nc))

    return dp[r][c]


N = int(input())
bamboo = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

count = 0

for r in range(N):
    for c in range(N):
        count = max(dfs(r, c), count)

print(count)