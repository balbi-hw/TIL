# SWEA - 4839 - 이진탐색


def binary_search(start, end, target):
    global whole

    count = 0

    if start == target:
        return count

    mid = (start + end) // 2

    if mid > target:
        count = max(count, binary_search(start, mid, target) + 1)
    else:
        count = max(count, binary_search(mid, end, target) + 1)

    return count


TC = int(input())
for test_case in range(1, TC+1):
    whole, Apage, Bpage = map(int, input().split())

    init_start = 1
    init_end = whole

    A_count = binary_search(init_start, init_end, Apage)
    B_count = binary_search(init_start, init_end, Bpage)

    if A_count == B_count:
        print(f"#{test_case} 0")
    elif A_count > B_count:
        print(f"#{test_case} B")
    else:
        print(f"#{test_case} A")