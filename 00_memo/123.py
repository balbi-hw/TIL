import sys

sys.stdin = open('input.txt')


def find_set(x):
    """
    x가 속한 집합의 대표자를 찾는 함수 (경로 압축 최적화 적용).
    x의 부모가 자기 자신이 아니라면, 재귀적으로 루트를 찾아 x의 부모로 직접 설정합니다.
    """
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    """
    두 원소 x, y가 속한 집합을 하나로 합치는 함수 (랭크 기반 최적화 적용).
    """
    root_x = find_set(x)
    root_y = find_set(y)

    # 두 원소의 대표자가 같다면, 이미 같은 집합이므로 합칠 필요가 없습니다.
    if root_x == root_y:
        return

    # 랭크(트리 높이)가 더 낮은 쪽을 더 높은 쪽 밑에 붙입니다.
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    else:
        parent[root_y] = root_x
        # 만약 랭크가 같다면, 한쪽의 랭크를 1 증가시킵니다.
        if rank[root_x] == rank[root_y]:
            rank[root_x] += 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pairs = list(map(int, input().split()))

    # make_set: 1부터 N까지, 각자 자기 자신을 대표자로 하는 집합을 만듭니다.
    parent = list(range(N + 1))
    # 모든 원소의 랭크를 0으로 초기화합니다.
    rank = [0] * (N + 1)

    # 주어진 모든 관계에 대해 union 연산을 수행합니다.
    for i in range(M):
        p1, p2 = pairs[i * 2], pairs[i * 2 + 1]
        union(p1, p2)

    # 최종 조의 개수를 찾기 위해 대표자들을 set에 담아 중복을 제거합니다.
    root_nodes = set()
    for i in range(1, N + 1):
        root_nodes.add(find_set(i))

    # 중복이 제거된 대표자들의 수가 곧 조의 개수입니다.
    print(f'#{tc} {len(root_nodes)}')
