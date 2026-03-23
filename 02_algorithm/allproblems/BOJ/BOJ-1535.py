# BOJ - 1535 안녕 한영욱.
# BYE BYE 한영욱! 건강해야해 !
# 나는 한영욱을 놓아주었다.

import sys
sys.setrecursionlimit(10**7)

def dfs(idx: int, life: int, cur_joy: int) -> None:
    global joy, N


    if life <= 0:
        return
    
    if idx == N:
        joy = max(joy, cur_joy)
        return

    l = lifes[idx]
    j = happeniss[idx]
    
    dfs(idx + 1, life, cur_joy)
    dfs(idx + 1, life - l, cur_joy + j)


N = int(input())
lifes = list(map(int, input().split()))
happeniss = list(map(int, input().split()))

joy = 0
dfs(0, 100, 0)

print(joy)