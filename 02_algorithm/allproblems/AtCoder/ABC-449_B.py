# ABC - 449 B

def eatting(order: int, num: int, chocolate: list) -> None:
    if order == 1:
        width = chocolate[1]
        eat_rightside = num
        print(width * eat_rightside)
        chocolate[0] -= eat_rightside

    else:
        height = chocolate[0]
        eat_bottom = num
        print(height * eat_bottom)
        chocolate[1] -= eat_bottom


H, W, Q = map(int, input().split())

chocolate = [H, W]

for _ in range(Q):
    order, num = map(int, input().split())

    eatting(order, num, chocolate)
