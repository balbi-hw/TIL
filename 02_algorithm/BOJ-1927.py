# BOJ - 1927 | 최소 힙
# https://www.acmicpc.net/problem/1927


import sys
import heapq

input = sys.stdin.readline

N = int(input())

pq = []

for _ in range(N):
    order = int(input())

    if order != 0:
        heapq.heappush(pq, order)
    else:
        if not pq:
            print(0)
        else:
            print(heapq.heappop(pq))