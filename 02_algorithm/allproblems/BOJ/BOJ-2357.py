# BOJ - 2357 - MinValue && MaxValue

import sys
input = sys.stdin.readline

def find_val(order: int, start: int, end: int, size: int, seg: list) -> int:

    start += size
    end += size

    val = seg[size]

    if order == 1:

        while start <= end:
            if start % 2 == 1:
                val = min(val, seg[start])
                start += 1
            
            if end % 2 == 0:
                val = min(val, seg[end])
                end -= 1

            start //= 2
            end //= 2

        return val

    if order == 2:

        while start <= end:
            if start % 2 == 1:
                val = max(val, seg[start])
                start += 1
            
            if end % 2 == 0:
                val = max(val, seg[end])
                end -= 1

            start //= 2
            end //= 2

        return val


N, M = map(int, input().split())
nums = [int(input().strip()) for _ in range(N)]

INF = 10**18

size = 1
while size < N:
    size *= 2

min_seg = [INF] * (2*size)
max_seg = [0] * (2*size)

for i in range(N):
    min_seg[size + i] = nums[i]

for i in range(N):
    max_seg[size + i] = nums[i]

for _ in range(M):
    start, end = map(int, input().split())
    start -= 1
    end -= 1

    for i in range(size-1, 0, -1):
        min_seg[i] = min(min_seg[i*2], min_seg[i*2+1])

    min_val = find_val(1, start, end, size, min_seg)
    
    for i in range(size-1, 0, -1):
        max_seg[i] = max(max_seg[i*2], max_seg[i*2+1])
    
    max_val = find_val(2, start, end, size, max_seg)

    print(min_val, max_val)
    