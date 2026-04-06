# BOJ-13913 | 숨바꼭질 4

from collections import deque

START, END = map(int, input().split())
MAX = 10 ** 5

dist = [-1] * (MAX + 1)
parent = [-1] * (MAX + 1)

dq = deque([START])
dist[START] = 0

while dq:
    current_position = dq.popleft()

    if current_position == END:
        break

    for next_position in (current_position - 1, current_position + 1, current_position * 2):
        if 0 <= next_position <= MAX and dist[next_position] == -1:
            dist[next_position] = dist[current_position] + 1
            parent[next_position] = current_position
            dq.append(next_position)
    
print(dist[END])

path = []
cur = END
while cur != -1:
    path.append(cur)
    cur = parent[cur]

print(*path[::-1])