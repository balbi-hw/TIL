# BOJ-14501
# 퇴사
# SW 달리기 // SILVER III

N = int(input())
sodann = [list(map(int, input().split())) for _ in range(N)]

result = 0

# 약간 dp인데
# 수영장 회원권 문제랑 비슷함

for i in range(N):
    k, m = sodann[i]
    if i + k > N:
        m = 0
        sodann[i] = [k, m]

print(sodann)

for idx in range(N):
    k, m = sodann[idx]

    sal = 0
    if idx + k <= N:
        for j in range(idx, idx+k):
            sal += sodann[j][1]
    print(sal)
    if m >= sal:
        result += m

print(result)