# 공을 k까지 꺼내고
# 안에 있는 것 중 가장 작은 수를 출력한다.
# 그리고 다시 다 넣는다.


import sys
input = sys.stdin.readline

INF = 10 ** 18

N, Q = map(int, input().split())
A = list(map(int, input().split()))

size = 1
while size < N:
    size *= 2

segment_tree = [INF] * (2 * size)

for i in range(N):
    segment_tree[size+i] = A[i]

for i in range(size-1, 0, -1):
    segment_tree[i] = min(segment_tree[i * 2], segment_tree[i * 2 + 1])

def update(idx, value):
    node = size + idx
    segment_tree[node] = value
    node //= 2
    while node:
        segment_tree[node] = min(segment_tree[node * 2], segment_tree[node * 2 + 1])
        node //= 2

for _ in range(Q):
    K = int(input())
    B = list(map(int, input().split()))

    removed = []
    for b in B:
        b -= 1
        removed.append(b)
        update(b, INF)

    print(segment_tree[1])

    for b in removed:
        update(b, A[b])