
# 전역변수
wordList = {}
player_nums = 0
words_nums = 0

def init(N, M, mWords):
    """
    단어를 객체로 하면 필드가

    class Word():
        def init(self, word):
            self.word = word
            self.used_time = 0
            self.revoked = False
    
        def use(self):
            if word == word[::-1]:
                self.used_time += 1        

        def update(self):
            if word == word[::-1]:
                if self.used_time = 1:
            if self.used_time = 2:
                self.revoked = True
    
    """

    """
    1. dict 로 알파벳 별 리스트를 구현한다.
        for alphabet in "abcdefghijklmnopqrstuvwxyz"
            dict[alphabet] = []
    2. mWords 를 순회하며 분류한다.
    """
    global wordList, player_nums, words_nums

    for ch in "abcdefghijklmnopqrstuvwxyz":
        wordList[ch] = []
    
    player_nums = N
    words_nums = M

    for word in mWords:
        ch = word[0]
        wordList[ch].append(word.obj)

    for ch in wordList.keys():
        wordList[ch].sort(key=lambda x: x.word)

    pass

def playRound(mID, mCh):
    """
    1. mID 번 부터 mCh 로 시작하는 단어중 사전 순 정렬된 첫 번째를 선택
    2. mID + 1 번 은 1번에서 선택한 단어의 마지막 Char 로 시작하는 단어를 선택
    3. 단어가 리스트[mWords] 내에 없다면 탈락.
    4. 다음 라운드 시작
    5. 이전 라운드에서 선택됐던 단어들의 스펠링 순서를 뒤집어서 다시 mWords 에 넣은 후 시작.
    6. 단어를 사용하면 뒤집는데 뒤집은 단어가 사용한 적이 있다면 폐기
    7. 6을 일일히 기록하기 힘들다.
        - 단어별로 사용 횟수를 기록해두고 palindrome 이라면 1번, 아니라면 2번 사용하면 폐기
    8. mWords 가 빌때까지 진행.
    """
    """
    자료구조 선택

    단순 리스트로 충분할 것 같다.
      - 단어를 찾아야하네, 찾는 게 일인 문제.
    
    알파벳마다 리스트를 하나씩 다 ?
    """
    global wordList

    cur_word_list = wordList

    nxt_word_list = {}

    wordList = nxt_word_list

    pass

# 소스코드와 같은 디렉토리에 input.txt 파일을 생성해서 거기에 입력을 넣은 뒤 아래 주석을 지우면 편하게 실행 가능합니다 :)
# fs = open("input.txt", "r")
# input = fs.readline

def run():
    ok = True
    N, M = map(int, input().split())
    mWords = [input().rstrip() for i in range(M)]

    init(N, M, mWords)

    cnt = int(input())
    for _ in range(cnt):
        line = input().split()

        mID = int(line[0])
        mCh = line[1]
        ret = playRound(mID, mCh)
        ans = int(line[2])

        if ret != ans:
            ok = False

    return ok

T, MARK = map(int, input().split())

for tc in range(1, T + 1):
    score = MARK if run() else 0
    print(f'#{tc} {score}')
