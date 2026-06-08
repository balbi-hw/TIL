import sys

sys.stdin = open("input.txt", "r")

"""
독서광 동철이는 책을 정말 꼼꼼히 읽는다. 그 증거로, 책에서 어떤 단어가 몇 번 등장하는지 물어보면 정확하게 그 답을 맞춰내는 신기한 능력이 있다.

그런데, 특출난 능력이 있으면 누군가는 시샘을 하게 마련이다.

동철이의 친구 영수는 동철이의 이런 능력을 의심하고 있었지만, 도저히 그 답이 맞는지 세어볼 수가 없어 당신에게 도움을 요청하였다.

영수의 궁금증을 해소해주기 위하여, 책의 내용 B가 주어질 때 특정 단어 S가 등장하는 횟수를 알아내어라.

책의 내용에서 특정 단어가 등장하는 부분이 중첩될 수도 있음에 유의하여라.

예를 들어, B="ABABA"이고 S="ABA"이면 2번 등장하는 것으로 간주한다.

---

첫 줄에 테스트케이스의 개수 T가 주어진다. (1 ≤ T ≤ 20)

각 테스트 케이스의 첫 번째 줄에 책의 내용 B가 주어진다.

책의 내용은 알파벳 소문자와 대문자, 그리고 숫자로만 이루어지고, 길이는 1 이상 500,000 이하이다.

각 테스트 케이스의 두 번째 줄에 찾고자 하는 단어 S가 주어진다.

찾고자 하는 단어는 알파벳 소문자와 대문자, 그리고 숫자로만 이루어지고, 길이는 1 이상 100,000 이하이다.
"""

"""
돌림 노래 같이 처리하면 어떨까?
객체를 하나씩 만들고 삭제하는거지
클래스 변수로 단어 개수를 만들고
인스턴스 변수로 카운팅을 하고 글자수가 찾고자 하는 단어 수랑 같아지면 클래스 변수 ++

최악은?
찾는 단어 길이 10만
똑같은 알파벳으로 길이 50만
그럼 한 번에 관리하는 객체 수가 최대 10만개?

제일 좋은건 정규식 사용하는 것 같은데

해싱?
슬라이딩 윈도우 하나 만들고 해싱하는건 어떤데?
해싱할 필요가 있나? 그냥 슬라이딩 윈도우 하나면 끝나는거 아님?

시간초과가 나네..
deque 로 만들어서 rotate 돌릴까

"""

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    # 0. 변수 초기화
    max_script_length = 500_000
    max_target_length = 100_000

    script = input().rstrip()
    target = input().rstrip()
    
    script_length = len(script)
    target_length = len(target)

    result = 0

    # deque.rotate 사용
    from collections import deque

    script = deque(list(script))
    script.rotate(1)

    for _ in range(script_length - target_length + 1):
        script.rotate(-1)
        current = "".join(list(script)[0:target_length])

        if current == target:
            result += 1

    print(f"#{test_case} {result}")

    # ///////////////////////////////////////////////////////////////////////////////////


# # V1 19/20 마지막 케이스 시간초과
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     # ///////////////////////////////////////////////////////////////////////////////////

#     # 0. 변수 초기화
#     max_script_length = 500_000
#     max_target_length = 100_000

#     script = input().rstrip()
#     target = input().rstrip()
    
#     script_length = len(script)
#     target_length = len(target)

#     result = 0

#     # 1. 슬라이딩 윈도우
#     for start in range(script_length - target_length + 1):
#         end = start + target_length

#         if script[start:end] == target:
#             result += 1

#     print(f"#{test_case} {result}")
#     # ///////////////////////////////////////////////////////////////////////////////////
