# ABC - 451 - B / Personal Change

N, M = map(int, input().split())

part_lst = [0] * (M+1)
for i in range(N):
    now, next = map(int, input().split())

    part_lst[now] -= 1
    part_lst[next] += 1

for num in part_lst[1:]:
    print(num)