# SWEA - 1873 | 상호의 배틀필드
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LyE7KD2ADFAXc


MAP = {
    "U": 0,
    "D": 1,
    "L": 2,
    "R": 3,
    "^": 0,
    "v": 1,
    "<": 2,
    ">": 3
}

TANK = ["^", "v", "<", ">"]

dirs =[
    (-1, 0), (1, 0), (0, -1), (0, 1)
]


def make_field() -> list[list[int]] | tuple[int]:
    field = []
    position = False
    for r in range(H):
        row = list(input())
        field.append(row)
        if not position:
            for i in "^v<>":
                if i in row:
                    position = (r, row.index(i))
                
    return field, position


def move(order: str, r: int, c: int) -> tuple:
    d = MAP[order]
    s = TANK[d]
    dr, dc = dirs[d]
    nr, nc = r + dr, c + dc

    field[r][c] = s

    if not (0 <= nr < H and 0 <= nc < W):
        return (r, c)

    if field[nr][nc] == ".":
        field[nr][nc] = s
        field[r][c] = "."

        return (nr, nc)

    return (r, c)
    

def fire(r: int, c: int) -> None:
    s = field[r][c]
    d = MAP[s]
    dr, dc = dirs[d]

    nr, nc = r + dr, c + dc
    while 0 <= nr < H and 0 <= nc < W:

        if field[nr][nc] in "#*":
            if field[nr][nc] == "*":
                field[nr][nc] = "."
            return

        nr, nc = nr + dr, nc + dc


def act(orders: list[str], position: tuple[int, int]) -> None:

    for order in orders:
        r, c = position

        if order in "UDLR":
            position = move(order, r, c)

        elif order == "S":
            fire(r, c)


TC = int(input())
for test_case in range(1, TC + 1):
    H, W = map(int, input().split())
    field, position = make_field()
    orders_time = int(input())
    orders = list(input())

    act(orders, position)

    print(f"#{test_case}", end=" ")
    for i in field:
        print("".join(i), sep="\n")