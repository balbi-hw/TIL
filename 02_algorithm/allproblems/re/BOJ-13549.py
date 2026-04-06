# BOJ-13549 | 숨바꼭질3
# https://www.acmicpc.net/problem/13549

from collections import deque

def calculate_next_position(pos: int) -> list[int]:
    return pos - 1, pos + 1, pos * 2


def bfs(START: int, END: int) -> int:

    MAX = 10 ** 5
    INF = float('inf')

    dq = deque([START])

    dist = [INF] * (MAX + 1)
    dist[N] = 0

    while dq:
        position = dq.popleft()

        if position == END:
            print(dist[position])
            
        minus, plus, multi = calculate_next_position(position)

        if 0 <= multi <= MAX and dist[multi] > dist[position]:
            dist[multi] = dist[position]
            dq.appendleft(multi)

        if 0 <= minus <= MAX and dist[minus] > dist[position] + 1:
            dist[minus] = dist[position] + 1
            dq.append(minus)

        if 0 <= plus <= MAX and dist[plus] > dist[position] + 1:
            dist[plus] = dist[position] + 1
            dq.append(plus)


N, K = map(int, input().split())
bfs(N, K)