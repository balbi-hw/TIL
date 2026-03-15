# BOJ - 2357 - MinValue && MaxValue

import sys
input = sys.stdin.readline

def find_val(start: int, end: int, size: int, seg: list) -> int:

    start += size
    end += size

    min_val = seg[start][0]
    max_val = seg[end][1]

    while start <= end:
        if start % 2 == 1:
            min_val = min(min_val, seg[start][0])
            max_val = max(max_val, seg[start][1])
            start += 1
        
        if end % 2 == 0:
            min_val = min(min_val, seg[end][0])
            max_val = max(max_val, seg[end][1])
            end -= 1

        start //= 2
        end //= 2

    return min_val, max_val


N, M = map(int, input().split())
nums = [int(input().strip()) for _ in range(N)]

INF = 10**18

size = 1
while size < N:
    size *= 2

seg = [[INF, 0] for _ in range(2*size)]

for i in range(N):
    seg[size + i][0] = nums[i]
    seg[size + i][1] = nums[i]

for i in range(size-1, 0, -1):
    seg[i][0] = min(seg[i*2][0], seg[i*2+1][0])
    seg[i][1] = max(seg[i*2][1], seg[i*2+1][1])

for _ in range(M):
    start, end = map(int, input().split())
    start -= 1
    end -= 1

    print(*find_val(start, end, size, seg))