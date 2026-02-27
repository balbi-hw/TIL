# BOJ-2565
# 전깃줄
# DP

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()
dp = [0] * N

for idx in range(N):
    a, b = lst[idx]
    for i in range(idx+1, N):
        if lst[i][1] < b:
            dp[i] += 1


    # if lst[i][1] < lst[i-1][1]:
    #     dp[i-1] += 1

if N == 1:
    print(0)
else:
    print(dp.count(0))