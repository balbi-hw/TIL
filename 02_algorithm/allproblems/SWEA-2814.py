# SWEA - 2814 | 최장 경로
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GOPPaAeMDFAXB&


def dfs(pos, depth):
    global count

    count = max(count, depth)

    for nxt in gragh[pos]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt, depth + 1)
            visited[nxt] = False


TC = int(input())
for test_case in range(1, TC + 1):
    N, M = map(int, input().split())

    gragh = [[] for _ in range(N + 1)]
    for _ in range(M):
        p, c = map(int, input().split())
        gragh[p].append(c)
        gragh[c].append(p)
    
    visited = [False] * (N + 1)
    count = 0

    for i in range(N):
        visited[i] = True
        dfs(i, 1)
        visited[i] = False
    
    print(f"#{test_case} {count}")