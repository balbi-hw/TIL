# SWEA - 16811
# 당근

# N개 당근
# 대 중 소 분류
# 한 상자에는 N // 2개 초과 들어가면 안된다
# 각 박스의 당근 개수 차이 최소화 및 차이 기록
# 크기를 입력값으로 받으면 자동으로 분류

# 박스는 대 중 소 1개씩 3개 고정이고
# 개수 조건을 초과하면 실패 -1 출력
# 성공하면 차이 출력
# import collections

def makeBox(num, i, j, lst):
    small = [lst[x] for x in range(i+1)]
    midium = [lst[x] for x in range(i+1, j+1)]
    large = [lst[x] for x in range(j+1, num)]

    return [small, midium, large]


TC = int(input())

for test_case in range(1, TC+1):
    carrot_num = int(input())
    carrot_size_list = list(map(int, input().split()))
    # ---------------- #

    carrot_size_list.sort()
    passed_box = []
    for i in range(carrot_num - 2):
        if carrot_size_list[i] == carrot_size_list[i + 1]:
            continue
        for j in range(i + 1, carrot_num - 1):
            if carrot_size_list[j] == carrot_size_list[j + 1]:
                continue
            # 함수?
            boxes = makeBox(carrot_num, i, j, carrot_size_list)
            
            for box in boxes:
                if len(box) > carrot_num // 2:
                    break
                else:
                    passed_box.append(boxes)
                    # 이 부분이 지금 문제
                    # 반복이 끝나면 추가해야하는데 하나만 넘어도 그냥 되고 있음

    if passed_box == False:
        print(-1)
        break

    max_len = 0
    min_len = 1000
    max_diff = 0
    for box in passed_box:
        for part in box:
            if len(part) < min_len:
                min_len = len(part)
            if len(part) > max_len:
                max_len = len(part)
        if max_diff < max_len - min_len:
            max_diff = max_len - min_len

    print(max_diff)        
    

            








#     small = []
#     middle = []
#     big = []

#     # 일단 균등하게 담을까? 아마 정렬 안되어서 줄거니까 정렬도 해두자
#     carrot_size_list.sort()

#     # for idx in range(carrot_num-1):
#     #     if carrot_size_list[idx] == 
#         # 딕셔너리로 할까?
#         # 딕셔너리로 묶어서 튜플로 꺼내자
#         # 그러면 묶이고 순서도 있어서 넣을 수 있고 그럼 되겠다
#         # 개수도 알 수 있고
#     # 그럼 count 불러올까
#     size_dict = collections.Counter(carrot_size_list)
#     size_tuple = list(size_dict.items())

#     # print(size_tuple)

#     # 당근 수 카운팅 변수
#     cnt_carrot = 0
#     # 그럼 len // 3 해서 그 만큼 박스에 담아야겠네
#     for size, num in size_tuple:
#         # 근데 크기가 같으면 같은 박스에 담아야하잖아
#         # 크기가 같으면 묶어버릴까?
#         # 어떻게?    
#         # 리스트로 저장해뒀다가 상자에 넣을 때 언패킹?
#         # 그럼 위에 가서 묶고 오자
#         if cnt_carrot < carrot_num // 3:
#             small.extend(size for _ in range(num))
#             cnt_carrot += num
#         elif cnt_carrot >= 2 * carrot_num // 3:
#             big.extend(size for _ in range(num))
#             cnt_carrot += num
#         else:
#             middle.extend(size for _ in range(num))
#             cnt_carrot += num
#         # 이렇게 하면 똑같은게 여러개 들어오면 계산을 못하네?
#         # 아니지 그럼 어차피 계산 실패니까 한곳에 다담겨서 -1 출렬기잖아


#     print(small, middle, big) 
#     boxes = [small, middle, big]
#     fail = 0
#     for box in boxes:
#         if len(box) > carrot_num // 2:
#             fail += 1

#     if fail == 0:    
#         vol_lst = list(map(len, boxes))
#         print(f'#{test_case} {max(vol_lst) - min(vol_lst)}')
#     else:
#         print(f'#{test_case} -1')


# # 1. 개수 분기를 size_dict 기준으로 했다