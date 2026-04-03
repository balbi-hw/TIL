# BOJ - 11003 | 최솟값 찾기

"""
슬라이딩 윈도우
"""

from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
numbers = list(map(int, input().split()))

dq = deque()
result = []
for i in range(N):
    while dq and numbers[dq[-1]] >= numbers[i]:
        dq.pop()

    dq.append(i)

    if dq[0] <= i - L:
        dq.popleft()

    result.append(numbers[dq[0]])

print(*result)