

def dfs(n):

    for i in info[n]:
        nn = i

        if not visited[i]:
            visited[nn] = True
            dfs(nn)


TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    edge = list(map(int, input().split()))

    info = [[] for _ in range(N + 1)]
    for i in range(M):
        p, c = edge[2 * i], edge[2 * i + 1]
        info[p].append(c)
        info[c].append(p)

    visited = [False] * (N + 1)
    count = 0

    for i in range(1, N+1):

        if not visited[i]:
            visited[i] = True
            count += 1
            dfs(i)
        
    print(f"#{test_case} {count}")