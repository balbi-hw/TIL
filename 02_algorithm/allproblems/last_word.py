"""
예외가 있다.

7번 게임 까지는 패스.

이후 게임들은 1라운드 확정 통과 -> 로직 문제 없음 ( 이후에도 통과가 있음 )

로직은 문제 없는 것 같고

예외가 몇 개 있나본데

1. Palindrome : 단어 객체 최초 생성할 때 확인하고 있음.


"""


# 클래스
class Word():

    def __init__(self, word):
        self.word = word

        if word == word[::-1]:
            self.reversed = True
        else:
            self.reversed = False

    def reverse(self):
        reversed_word = self.word[::-1]
        new_word = Word(reversed_word)
        new_word.reversed = True
        return new_word


# 전역변수
word_dict = {}
point_dict = {}
player_nums = 0
words_nums = 0
out_player = []

def init(N, M, mWords):
    """
    1. dict 로 알파벳 별 리스트를 구현한다.
        for alphabet in "abcdefghijklmnopqrstuvwxyz"
            dict[alphabet] = []
    2. mWords 를 순회하며 분류한다.
    """
    global word_dict, point_dict, player_nums, words_nums, out_player

    word_dict = {}

    for ch in "abcdefghijklmnopqrstuvwxyz":
        word_dict[ch] = []
    
    player_nums = N
    words_nums = M

    out_player = [False] * (N + 1)

    for word in mWords:
        ch = word[0]
        word = Word(word)
        word_dict[ch].append(word)


    pass

def playRound(mID, mCh):
    global word_dict

    # print("정렬 전", word_dict)
    for ch in word_dict.keys():
        word_dict[ch].sort(key=lambda x: x.word)
    # print("정렬 후", word_dict)
        

    point_dict = {}
    nxt_word_dict = {}

    for ch in "abcdefghijklmnopqrstuvwxyz":
        point_dict[ch] = 0
        nxt_word_dict[ch] = []
        
    cur_word_dict = word_dict

    cur_player = mID
    cur_ch = mCh

    while True:

        # if out_player[cur_player]:
        #     cur_player += 1
        #     if cur_player > player_nums:
        #         cur_player %= player_nums
        #     continue

        # print(f"{cur_player}번님의 차례입니다.")

        pointer = point_dict[cur_ch]

        try:
            cur_word = cur_word_dict.get(cur_ch, None)[pointer]  # IndexError

            # print(f"현재 단어: {cur_word.word}")
            
            reversed_word = cur_word.reverse()

            ch = reversed_word.word[0]

            point_dict[cur_ch] += 1
            cur_ch = ch

            if not cur_word.reversed:  # TypeError
                nxt_word_dict[ch].append(reversed_word)

        # except IndexError, TypeError:
        except IndexError:
            word_dict = nxt_word_dict

            for ch in "abcdefghijklmnopqrstuvwxyz":
                pointer = point_dict[ch]

                # if ch not in word_dict:
                #     word_dict[ch] = []

                word_dict[ch].extend(cur_word_dict[ch][pointer:])

            out_player[cur_player] = True
            return cur_player
        
        # print("통과")
        def get_next_player(cur_player):
            cur_player += 1

            if cur_player > player_nums:
                cur_player = 1

            while out_player[cur_player]:
                cur_player += 1

                if cur_player > player_nums:
                    cur_player = 1

            return cur_player
        
        cur_player = get_next_player(cur_player)
        # cur_player += 1

        # if cur_player > player_nums:
        #     cur_player %= player_nums

        # while out_player[cur_player]:
        #     cur_player += 1

        # if cur_player == player_nums:
        #     continue
        # else:
        #     cur_player %= player_nums


# 소스코드와 같은 디렉토리에 input.txt 파일을 생성해서 거기에 입력을 넣은 뒤 아래 주석을 지우면 편하게 실행 가능합니다 :)
fs = open("input.txt", "r")
input = fs.readline

def run():
    ok = True
    N, M = map(int, input().split())
    mWords = [input().rstrip() for i in range(M)]

    init(N, M, mWords)

    cnt = int(input())
    for i in range(cnt):
        line = input().split()

        mID = int(line[0])
        mCh = line[1]
        ret = playRound(mID, mCh)
        ans = int(line[2])

        if ret != ans:
            print(f"{i + 1} 라운드 {ret}가 탈락하였습니다. 정답은 {ans} 입니다.")
            ok = False
        else:
            print(f"{i + 1} 라운드 통과입니다.")

    return ok

T, MARK = map(int, input().split())

for tc in range(1, T + 1):
    score = MARK if run() else 0
    print(f'#{tc} {score}')
