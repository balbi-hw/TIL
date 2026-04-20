'''
N 을 리스트로 받은 다음에 하나하나 체크하고 while 문에서 전체 요소에 map 으로 전체에 곱해주고 다시 체크

아니 무슨 질문이; 직관적으로 알 수 있는거잖아 그냥 억지질문 에바임요


'''

# TC = int(input())
# for test_case in range(1, TC + 1):
#     N = int(input())
#     cur_state = (1 << (N + 1)) - 1 


#     target = (1 << 10) - 1

#     time = 1

#     result = 0

#     while result & target != target:

#         value = (1 << N * time) - 1

#         result = result | ((1 << N*time) - 1)

#         time += 1

#     # if result & target == target:
#     #     print(time)

#     print(time)



TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int, input().split())

    goal = (1 << N) - 1

    result = M & goal

    if result == goal:
        print(f"#{test_case} ON")
    else:   
        print(f"#{test_case} OFF")


"""
확인할 것

1. New 연산자 > 무겁다 !!
2. 동적 할당 // 정적 할당 -> 그냥 정적배열을 개크게 만들어둔다.



"""