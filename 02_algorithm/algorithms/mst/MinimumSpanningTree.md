# Minimum Spanning Tree, 최소 신장 트리

## 목차
    - [신장 트리?](#spanning-tree-신장-트리)
    - [최소 신장 트리?](#mst)
    - 주요 알고리즘
        - [Kruskal](#kruskal-알고리즘)
        - [Prim](#prim-알고리즘)
    - [연습문제](#연습문제)

## Spanning Tree, 신장 트리
- n 개의 정점으로 이루어진 무향 그래프에서 n개의 정점과 n-1 개의 간선으로 이루어진 트리

## MST
- 무향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리
- 그래프에서 최소 비용 문제이다. ( 탐욕 )

## Kruskal 알고리즘
1. 간선을 하나씩 선택해서 MST 를 찾는다.
2. 모든 간선을 가중치에 따라 오름차순 정렬 후 시작
3. 가중치가 가장 낮은 간선부터 선택
    - 선택한 간선의 두 정점에 대해 아래 상황에 따라 진행
        1. 두 태표자가 다르다면 엣지를 최소비용집합에 추가
        2. 두 대표자가 같다면 사이클이 생성되니 무시
4. n-1 개의 간선이 선택될때까지 2번 과정을 반복
```python
if find_set(a) != find_set(b):
    union(a, b)
else:
    continue
```
5. 코드 구현
```python
class DisjointSet:
    def __init__(self, v):
        self.p = [0] * (len(v) + 1)

    def make_set(self, x):
        self.p[x] = x
    
    def find_set(self, x):
        if x != self.p[x]:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)

        if px < py:
            self.p[py] = px
        else:
            self.p[px] = py

def mst_kruskal(vertixes, edges):
    mst = []
    n = len(vertixes)
    ds = DisjointSet(vertixes)

    for i in range(n + 1):
        ds.make_set(i)
    
    edges.sort(key=lambda x: x[2])
    for edge in edges:
        s, e, w = edge
        if ds.find_set(s) != ds.find_set(e):
            ds.unioun(s, e)
            mst.append(edge)
    return mst

edges = [[1, 2, 1], [2, 3, 3], [1, 3, 2]]
vertixes = [1, 2, 3]
mst_kruskal(vertixes, edges)

```

### 정리
- 특징
    1. 탐욕
    2. 간선을 가중치 순으로 정렬하여 처리
    3. Disjoint 를 사용해 사이클 형성 방지
- 장점
    1. 희소 그래프에서 효율적
    2. 간선 중심 알고리즘
    3. 음의 가중치도 처리 가능
- 단점
    1. 간선 정렬이 필요함
    2. 동적 그래프에 적용하기 어려움
- 시간복잡도
    - O(E logE) or O(E logV)

---

## Prim 알고리즘
- 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만든다.
    1. 임의 정점을 하나 선택
    2. **우선순위 큐**를 사용해 간선의 가중치가 가장 작은 간선 선택
    3. 가장 가중치가 작은 간선을 선택하고 이 간선 넘어의 정점이 방문한 정점이 아니라면 해당 간선을 MST에 추가하고 방문처리.
    4. 큐가 빌때까지 반복

- 코드 구현
```python
import heapq

def prin(vertixes, edges):
    mst = []

    adj_list = {v: [] for v in vertixes}
    for start_v, end_v, w in edges:
        adj_list[start_v].append((end_v, w))
        adj_list[end_v].append((start_v, w))

    visited = set()
    init_vertex = vertixes[0]
    min_heap = [[w, init_vertex, e] for e, w in adj_list[init_vertx]]
    heapq.heapify(min_heap)
    visited.add(init_vertex)

    while min_heap:
        weight, start_v, end_v = heapq.heappop(min_heap)
        if end_v in visited:
            continue

        visited.add(end_v)
        mst.append((start_v, end_v, weight))

        for adj_v, adj_w in adj_list[end_v]:
            if adj_v in visited:
                continue
            heapq.heappush(min_heap, [adj_w, end_v, adj_v])
    
    return mst

vertixes = [1, 2, 3]
edges = [[1, 2, 30], [2, 3, 20], [1, 3, 10]]
mst = prim(vertixes, edges)
```

### 정리
- 특징
    1. 탐욕
    2. 각 단계에서 인접한 간선 중 가장 가중치가 작은 간선 선택
- 장점
    1. 밀집 그래프에서 효과적
    2. 정점 중심의 알고리즘
- 단점
    1. 희소 그래프에서 비효율적

## 연습문제
1. [BOJ - 9372](https://www.acmicpc.net/problem/9372)
```python
# BOJ - 9372 상근이의 여행
# MST 연습 문제

def make_set(x):
    parent[x] = x

def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]

def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px == py:
        return False

    if px < py:
        parent[py] = px
    else:
        parent[px] = py

    return True


TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    parent = list(range(N + 1))
    # 2차원 리스트

    count = 0
    for i in range(M):
        p, c = map(int, input().split())
        if union(p, c):
            count += 1
    
    print(count)

#####
'''
정답.

TC = int(input())
for _ in range(TC):
    N, M = map(int, input().split())
    for _ in range(M):
        input()
    print(N - 1)
'''
```
MST 연습에 매몰되어 간단한 정답을 놓쳤다.  
`모든 국가를 연결하는 최소 간선 수` 는 `Spanning Tree` 이므로 항상 `N-1` 이 됩니다.  
위의 `DisjointSet` 구현 방식도 정답은 나오지만 테스트케이스의 수가 많아지면 아마 시간초과가 날 수도 있어보인다.