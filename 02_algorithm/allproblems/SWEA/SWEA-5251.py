# SWEA - 5251 | 최소 이동 거리
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


import heapq

# 그래프 구현 함수
def make_route() -> list:

    route = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        route[s].append((e, w))

    return route

# 거리 계산 함수 ( 다익스트라 )
def calculate_dist(route: list) -> int:

    dist = [float('inf') for _ in range(N + 1)]
    dist[0] = 0

    pq = []
    heapq.heappush(pq, (0, 0))

    while pq:
        cur_weight, cur_position = heapq.heappop(pq)

        if cur_weight > dist[cur_position]:
            continue

        for nxt_position, weight in route[cur_position]:
            nxt_weight = cur_weight + weight

            if nxt_weight < dist[nxt_position]:
                dist[nxt_position] = nxt_weight
                heapq.heappush(pq, (nxt_weight, nxt_position))

    return dist[N]


TC = int(input())
for test_case in range(1, TC + 1):
    N, E = map(int, input().split())

    route = make_route()
    
    print(f"#{test_case} {calculate_dist(route)}")