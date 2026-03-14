# BOJ - 11505 - 구간 곱 구하기

import sys
input = sys.stdin.readline

'''
구간 합 구하기 문제에서 덧셈을 곱셈으로만 바꿔주면 되는 문제
모든 값에 MOD 연산을 해주어야한다. 안그럼 터진다.
'''

MOD = 1000000007

def update(idx: int, value: int):
    global seg, size

    idx += size
    seg[idx] = value % MOD

    node = idx // 2

    while node > 0:
        seg[node] = (seg[2*node] * seg[2*node + 1]) % MOD
        node //= 2


def query(start: int, end: int):
    global seg

    start += size
    end += size
    result = 1

    while start <= end:
        if start % 2 == 1:
            result = (result * seg[start]) % MOD
            start += 1
        
        if end % 2 == 0:
            result = (result * seg[end]) % MOD
            end -= 1
        
        start //= 2
        end //= 2

    return result


N, M, K = map(int, input().split())
nums = [int(input().strip()) for _ in range(N)]

size = 1
while size < N:
    size *= 2

seg = [1] * (2 * size)

for i in range(N):
    seg[size+i] = nums[i] % MOD

for i in range(size-1, 0, -1):
    seg[i] = (seg[2*i] * seg[2*i+1]) % MOD
    

for _ in range(M+K):
    order, B, C = map(int, input().split())
    B -= 1

    if order == 1:
        update(B, C)

    else:
        C -= 1
        print(query(B, C))
