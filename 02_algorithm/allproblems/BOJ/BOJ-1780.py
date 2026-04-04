# BOJ - 1780 | 종이의 개수
# https://www.acmicpc.net/problem/1780

def divide_paper(r: int, c: int, n: int) -> None:
    global result

    value = paper[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if paper[i][j] != value:
                m = n // 3                
                divide_paper(r, c, m)
                divide_paper(r + m, c, m)
                divide_paper(r + 2*m, c, m)
                divide_paper(r + 2*m, c + m, m)
                divide_paper(r, c + m, m)
                divide_paper(r, c + 2*m, m)
                divide_paper(r + m, c + 2*m, m)
                divide_paper(r + m, c + m, m)
                divide_paper(r + 2*m, c + 2*m, m)
                return

    result[value + 1] += 1


N = int(input().strip())
paper = [list(map(int, input().split())) for _ in range(N)]

result = [0, 0, 0]
divide_paper(0, 0, N)

for i in range(3):
    print(result[i])