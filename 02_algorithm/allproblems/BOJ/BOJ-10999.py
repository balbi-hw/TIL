# BOJ - 10999 구간 합 구하기 2
# 느리게 갱신되는 세그먼트 트리?

import sys
input = sys.stdin.readline

def update(start: int, end: int, val: int) -> None:
    global seg, size

    start += size
    end += size

    for i in range(start, end+1):
        seg[i] += val
        i //= 2
        while i > 0:
            seg[i] += val
            i //= 2


def cal(start: int, end:int) -> None:
    global seg, size

    start += size
    end += size

    result = 0
    while start <= end:
        if start % 2 == 1:
            result += seg[start]
            start += 1

        if end % 2 == 0:
            result += seg[end]
            end -= 1
        
        start //= 2
        end //= 2

    return result


N, M, K = map(int, input().split())
# nums = [int(input().strip()) for _ in range(N)]

size = 1
while size < N:
    size *= 2

seg = [0] * (2 * size)

for i in range(N):
    seg[i+size] = int(input().strip())

for i in range(size-1, 0, -1):
    seg[i] = seg[i*2] + seg[i*2+1]

for _ in range(M + K):
    query = list(map(int, input().split()))

    order = query[0]

    if order == 1:
        start, end, val = query[1:4]
        start -= 1
        end -= 1
        update(start, end, val)

    else:
        start, end = query[1:3]
        start -= 1
        end -= 1
        print(cal(start, end))
