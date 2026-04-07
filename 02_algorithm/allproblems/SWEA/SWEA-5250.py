# SWEA - 5250 | 최소 비용
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


import heapq


dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]


def calculate_fuel() -> int:

    cost = [[INF] * (N) for _ in range(N)]
    cost[0][0] = 0

    START = (0, 0)
    END = (N - 1, N - 1)

    pq = []
    heapq.heappush(pq, (0, START))

    while pq:
        cur_fuel, position = heapq.heappop(pq)
        
        r, c = position

        if cur_fuel > cost[r][c]:
            continue

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < N and 0 <= nc < N):
                continue

            if field[nr][nc] > field[r][c]:
                nxt_fuel = cur_fuel + field[nr][nc] - field[r][c] + 1
            else:
                nxt_fuel = cur_fuel + 1

            if nxt_fuel < cost[nr][nc]:
                cost[nr][nc] = nxt_fuel
                heapq.heappush(pq, (nxt_fuel, (nr, nc)))

    return cost[N-1][N-1]


TC = int(input())
for test_case in range(1, TC + 1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    INF = float('inf')

    print(f"#{test_case} {calculate_fuel()}")