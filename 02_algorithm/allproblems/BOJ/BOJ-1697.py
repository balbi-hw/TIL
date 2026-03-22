# BOJ - 1697 숨바꼭질
# https://www.acmicpc.net/problem/1697

from collections import deque

def bfs(n, k):
    MAX = 100000

    q = deque([(n, 0)])
    visited = [False] * (MAX + 1)
    visited[n] = True

    while q:
        n, t = q.popleft()

        if n == k:
            return t
        
        for nn in (n -1, n+ 1, n * 2):
            if 0 <= nn <= MAX and not visited[nn]:
                visited[nn] = True
                q.append((nn, t + 1))


N, K = map(int, input().split())
print(bfs(N, K))