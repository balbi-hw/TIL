# BOJ - 15686 | 치킨 배달
# https://www.acmicpc.net/problem/15686

import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

houses = []
chickens = []

for r in range(N):
    row = list(map(int, input().split()))
    for c in range(N):
        if row[c] == 1:
            houses.append((r, c))
        elif row[c] == 2:
            chickens.append((r, c))

answer = float("inf")

for selected in combinations(chickens, M):
    city_distance = 0

    for hr, hc in houses:
        chicken_distance = float("inf")

        for cr, cc in selected:
            dist = abs(hr - cr) + abs(hc - cc)
            chicken_distance = min(chicken_distance, dist)

        city_distance += chicken_distance

    answer = min(answer, city_distance)

print(answer)