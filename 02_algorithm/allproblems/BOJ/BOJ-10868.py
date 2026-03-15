# BOJ - 10868 - MinValue
# 해결 성공, 더 개선할 사항이 있는지 확인 요함

import sys
input = sys.stdin.readline


def find_min(start: int, end: int):
    global seg, size

    start += size
    end += size

    result = seg[start]

    while start <= end:
        if start % 2 == 1:
            result = min(result, seg[start])
            start += 1
        # else:
        #     seg[start//2] = min(seg[start], seg[start+1])
        
        if end % 2 == 0:
            result = min(result, seg[end])
            end -= 1
        # else:
        #     seg[end//2] = min(seg[end], seg[end-1])
        
        start //= 2
        end //= 2

    return result


N, M = map(int, input().split())
nums = [int(input().strip()) for _ in range(N)]

INF = 10**18

size = 1
while size < N:
    size *= 2

seg = [INF] * (2 * size)

for i in range(N):
    seg[i+size] = nums[i]

for i in range(size-1, 0, -1):
    seg[i] = min(seg[i*2], seg[i*2+1])

for _ in range(M):
    start, end = map(int, input().split())
    start -= 1
    end -= 1

    print(find_min(start, end))