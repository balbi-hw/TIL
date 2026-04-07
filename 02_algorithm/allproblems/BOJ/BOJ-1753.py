# BOJ - 1753 | 최단경로
# https://www.acmicpc.net/problem/1753

import sys
input = sys.stdin.readline

import heapq


def make_info() -> list[int]:

    info = [[] for _ in range(V + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        info[s].append((e, w))
    
    return info


def make_cheapest(route: list) -> list[int]:

    dist = [float('inf')] * (V + 1)
    dist[START] = 0

    pq = []
    heapq.heappush(pq, (0, START))

    while pq:
        cur_weight, cur_position = heapq.heappop(pq)

        if cur_weight > dist[cur_position]:
            continue

        for nxt_position, weight in route[cur_position]:
            nxt_weight = cur_weight + weight
            if nxt_weight < dist[nxt_position]:
                dist[nxt_position] = nxt_weight
                heapq.heappush(pq, (nxt_weight, nxt_position))

    return dist[1:]


V, E = map(int, input().split())
START = int(input())

info = make_info()
result = make_cheapest(info)

for i in result:
    if i == float('inf'):
        print("INF")
    else:
        print(i)