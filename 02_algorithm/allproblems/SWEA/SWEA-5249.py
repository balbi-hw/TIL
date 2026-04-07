# SWEA - 5249 | 최소 신장 트리
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):

    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        parent[root_y] = parent[root_x]
        return True
    return False



TC = int(input())
for test_case in range(1, TC + 1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    edges.sort(key=lambda x: x[2])

    parent = list(range(V + 1))

    mst_weight = 0
    edge_count = 0

    for n1, n2, weight in edges:
        if union(n1, n2):
            mst_weight += weight
            edge_count += 1

            if edge_count == V:
                break

    print(f"#{test_case} {mst_weight}")