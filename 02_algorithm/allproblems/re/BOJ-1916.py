# BOJ - 1916 | 최소비용 구하기
# https://www.acmicpc.net/problem/1916

import heapq
import sys
input = sys.stdin.readline

def make_route() -> list[int]:
    
    info = [[] for _ in range(number_of_village + 1)]
    for _ in range(number_of_bus):
        start, end, cost = map(int, input().split())
        info[start].append((end, cost))
    
    return info


def calculation_cheapest(route: list) -> int:

    departure, arrival = map(int, input().split())

    cost = [float('inf')] * (number_of_village + 1)
    cost[departure] = 0

    priority_queue = []
    heapq.heappush(priority_queue, (0, departure))

    while priority_queue:
        cur_cost, position = heapq.heappop(priority_queue)

        if cur_cost > cost[position]:
            continue

        for next_position, weight in route[position]:
            new_cost = cur_cost + weight

            if new_cost < cost[next_position]:
                cost[next_position] = new_cost
                heapq.heappush(priority_queue, (new_cost, next_position))

    return cost[arrival]


number_of_village = int(input())
number_of_bus = int(input())

route = make_route()

print(calculation_cheapest(route))