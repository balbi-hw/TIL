# SWEA - 5205 - Quick Sort

def quick_sort(start: int, end: int, arr: list):

    if start < end:
        pivot_idx = partition(start ,end, arr)

        quick_sort(start, pivot_idx - 1, arr)
        quick_sort(pivot_idx + 1, end, arr)


def partition(start, end, arr):
    pivot = arr[end]

    i = start - 1

    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[i+1], arr[end] = arr[end], arr[i+1]

    return i + 1


TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(0, N-1, arr)

    print(f"#{test_case} {arr[N//2]}")