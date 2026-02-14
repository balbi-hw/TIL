# SWEA - 2115
# 벌꿀채취
# 2041

import sys
sys.stdin = open('z.txt')

def dfs(l, r, c, now, val):
    global revenue
    if now > C:
        return
    if l == M:
        revenue = max(revenue, val)
    else:
        dfs(l + 1, r, c+1, now + honey[r][c], val + honey[r][c]**2)
        dfs(l + 1, r, c+1, now, val)


T = int(input())

for t in range(1, T+1):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]

    revenue = 0
    revenue_a = 0
    revenue_b = 0
    result = 0

    for r1 in range(N):
        for c1 in range(N-M+1):
            revenue = 0
            dfs(0, r1, c1, 0, 0)
            revenue_a = revenue
            
            for r2 in range(r1, N):
                start = 0
                if r1 == r2:
                    start = c1 + M
                for c2 in range(start, N-M+1):
                    revenue = 0
                    dfs(0, r2, c2, 0, 0)
                    revenue_b = revenue

                    result = max(result, revenue_a + revenue_b)
    
    print(f'#{t} {result}')


    