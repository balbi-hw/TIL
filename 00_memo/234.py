

def find_set(node):
    if parent[node] != node:
        parent[node] = find_set(parent[node])
    return parent[node]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:
        return
    
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    else:
        parent[root_y] = root_x
        # 둘 중 하나의 랭크를 높여야하는데 y를 x에 붙였으니 x를 올린다.
        if rank[root_x] == rank[root_y]:
            rank[root_x] += 1


TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    edge = list(map(int, input().split()))

    parent = list(range(N + 1))
    rank = [0] * (N + 1)

    for i in range(M):
        p1, p2 = edge[i * 2], edge[i * 2 + 1]
        union(p1, p2)

    root_nodes = set()
    for i in range(1, N + 1):
        root_nodes.add(find_set(i))

    print(f"#{test_case} {len(root_nodes)}")