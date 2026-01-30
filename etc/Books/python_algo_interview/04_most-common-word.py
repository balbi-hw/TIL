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
    
    counts = collections.Counter(words)
    # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴 (교재 내 작성되어 있는 내용)
    return counts.most_common(1)[0][0]

print(mostCommonWord(paragraph = "Bob hit a ball, the git BALL flew far after it was hit.", banned = ["hit"]))

#-----------------------------------------#

'''
구두점을 무시하기 위해 regex 모듈로 구두점을 모두 제거했고 .lower() 메서드를 이용해 대문자를 소문자로 변경했다.
이 과정을 '데이터 클렌징'이라고 부르며 입력값에 대한 '전처리' 작업이라고 한다.
[^\w] 는 단어문자가 아닌 전체를 의미한다. 즉 위 코드에서 정규식은 단어문자가 아닌 모든 문자를 공백으로 치환하는 역할을 한다.

19번 라인이 설명을 봐도 잘 이해가 안된다. collections 모듈의 개념이 모자라다.
추후 다시 보자

모듈과 라이브러리의 차이도 잘 모르겠다.

'''