# 타카바시군은 후추가 좋다.
# 뿌릴 수 있는 후추 최댓값

N, M = map(int, input().split())
C = list(map(int, input().split()))
dishes = [tuple(map(int, input().split())) for _ in range(N)]

amount = 0
for a, b in dishes:
    if C[a-1] <= b:
        amount += C[a-1]
        C[a-1] = 0
    else:
        amount += b
        C[a-1] -= b

print(amount)