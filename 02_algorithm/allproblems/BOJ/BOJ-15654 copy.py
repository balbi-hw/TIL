# BOJ - 15654  N과 M
# 실패

import sys
input = sys.stdin.readline

def dfs():
    if len(path) == M:
        print(*path)

    for i in range(N):
        if visited[i]:
            continue

        visited[i] = True
        path.append(nums[i])

        dfs()

        path.pop()
        visited[i] = False


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [False] * N
path = []

dfs()