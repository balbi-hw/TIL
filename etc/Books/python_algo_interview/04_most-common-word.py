# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
# 대소문자 구분을 하지 않으며, 구두점 또한 무시한다.

# 입력
# paragraph = "Bob hit a ball, the git BALL flew far after it was hit,"
# banned = ["hit"]

# 출력
# "ball"

import re
import collections

def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
             .lower().split()
                    if word not in banned]
    # paragraph 에서 regex로 구두점을 다 지우고 .lower() 로 대문자 소문자로 바꾸고
    # .split() 으로 공백 기준으로 나눠 리스트화 후 banned 리스트에 각 요소가 없으면 words 리스트에 추가

    print(words) # 확인용 코드 추가
    counts = collections.Counter(words) # collections 모듈의 counter 클래스를 이용해 숫자를 세고 dict 화
    # collections.counter() 는 defaultdict() 기능이 있다.
    print(counts)
    # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴 (교재 내 작성되어 있는 내용)
    return counts.most_common(1)[0][0]
    # .most_common(n) 메서드는 객체 안에서 n번째 많은 순서만큼 출력한다. 뒤의 index는 1번째로 출력된 튜플 중 0번 튜플의 0번 인덱스 값

    ###########
    ## !!!!! ##
    ## !!!!! ##
    ###########
    # .most_common()은 Counter()클래스의 메서드이다. 즉 counter()가 아닌 객체에는 사용할 수 없다. 그런데 counts 에는 사용했다. 왜일까?
    # 그리고 counts를 출력해보면 딕셔너리 형태로 나오는데 어떻게 빈도수를 뽑아내는 most_common() 메서드를 사용할 수 있을까. 왜일까?
    #
    # 이는 객체 개념이 들어가있다. counts 의 값을 보면 collections.Counter()로 정의되어있다. 그럼 counts.most_common()이 입력되면
    # counts가 collections.Counter()로 바뀌어 연산을 진행한다.
    # 즉 counts.most_common(1)[0][0] == collections.Counter().most_common(1)[0][0]이 되는 것이다.
    # 그 말은 counts가 collections.Counter 를 이용해 만들어진 dict가 아니고 그냥 같은 내용으로 정의된 변수였다면 .most_common() 메서드를 사용할 수 없다는 뜻
    

print(mostCommonWord(paragraph = "Bob hit a ball, the git BALL flew far after it was hit.", banned = ["hit"]))

#-----------------------------------------#

'''
구두점을 무시하기 위해 regex 모듈로 구두점을 모두 제거했고 .lower() 메서드를 이용해 대문자를 소문자로 변경했다.
이 과정을 '데이터 클렌징'이라고 부르며 입력값에 대한 '전처리' 작업이라고 한다.
[^\w] 는 단어문자가 아닌 전체를 의미한다. 즉 위 코드에서 정규식은 단어문자가 아닌 모든 문자를 공백으로 치환하는 역할을 한다.

19번 라인이 설명을 봐도 잘 이해가 안된다. collections 모듈의 개념이 모자라다.
//
collections 를 불러와서 counter를 사용하는 것
# from collections import counter 과의 차이

모듈과 라이브러리의 차이도 잘 모르겠다. // 쓰다보면 구분 가능하게 된다고 하니까 특별히 의미를 둘 필요는 없을 듯

'''