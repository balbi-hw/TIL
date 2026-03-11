# SWEA - 5204 - Merge Sort

def merge(left_sorted, right_sorted):
    global count


    merged_list = []
    left_point = right_point = 0

    while left_point < len(left_sorted) and right_point < len(right_sorted):
        if left_sorted[left_point] < right_sorted[right_point]:
            merged_list.append(left_sorted[left_point])
            left_point += 1
        else:
            merged_list.append(right_sorted[right_point])
            right_point += 1
    
    merged_list.extend(left_sorted[left_point:])
    merged_list.extend(right_sorted[right_point:])

    return merged_list


def merge_sort(arr: list):
    global count

    # 하나만 남을 때까지 반반 나눈다.
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    if left_sorted[-1] > right_sorted[-1]:
        count += 1    
        
    return merge(left_sorted, right_sorted)


TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))

    count = 0

    merged_arr = merge_sort(arr)

    print(f"#{test_case} {merged_arr[N//2]} {count}")