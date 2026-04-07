# SWEA - 1249 | 보급로
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15QRX6APsCFAYD

import heapq


dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]


def make_route() -> int:

    INF = float('inf')
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = 0

    pq = []
    heapq.heappush(pq, (0, (0, 0)))

    while pq:
        cur_time, cur_position = heapq.heappop(pq)
        r, c = cur_position

        if cur_time > dist[r][c]:
            continue

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < N and 0 <= nc < N):
                continue

            nxt_time = field[nr][nc] + cur_time
            if nxt_time < dist[nr][nc]:
                dist[nr][nc] = nxt_time
                heapq.heappush(pq, (nxt_time, (nr, nc)))

    return dist[N-1][N-1]


TC = int(input())
for test_case in range(1, TC + 1):
    N = int(input())
    field = [list(map(int, list(input()))) for _ in range(N)]

    print(f"#{test_case} {make_route()}")