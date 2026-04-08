# BOJ - 1504 | 특정한 최단 경로
# https://www.acmicpc.net/problem/1504

import sys
import heapq

input = sys.stdin.readline


def bfs(start):
    dist = [INF] * (V + 1)
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_dist, cur_position = heapq.heappop(pq)

        if cur_dist > dist[cur_position]:
            continue

        for nxt_position, new_dist in gragh[cur_position]:
            nxt_dist = new_dist + cur_dist

            if nxt_dist < dist[nxt_position]:
                dist[nxt_position] = nxt_dist
                heapq.heappush(pq, (nxt_dist, nxt_position))

    return dist

V, E = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(E)]
INF = float('inf')

gragh = [[] for _ in range(V + 1)] 
for s, e, d in info:
    gragh[s].append((e, d))
    gragh[e].append((s, d))

v1, v2 = map(int, input().split())

dist1 = bfs(1)
distv1 = bfs(v1)
distv2 = bfs(v2)

path1 = dist1[v1] + distv1[v2] + distv2[V]
path2 = dist1[v2] + distv2[v1] + distv1[V]

result = min(path1, path2)

if result >= INF:
    print(-1)
else:
    print(result)