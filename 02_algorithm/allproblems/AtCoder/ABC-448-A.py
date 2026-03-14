# 길이 N의 정수열 A와 정수 X가 주어진다.
# N이하의 자연수 i
# A[i] < X 라면 X = A[i]로 갱신되고 1을 출력
# 그렇지 않으면 0 출력

N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in A:
    if i < X:
        X = i
        print(1)
    else:
        print(0)