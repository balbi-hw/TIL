

class Member():
    def __init__(self, mID, mTeam, mScore, version):
        self.id = mID
        self.team = mTeam
        self.score = mScore
        self.next = None

        ###
        self.version = version
        pass


class Team():

    def __init__(self):
        self.members = [LinkedList() for _ in range(6)]

    def update(self, score):
        new_members = [LinkedList() for _ in range(6)]
        for i in range(1, 6):
            idx = i + score
            if idx > 5:
                idx = 5
            elif idx < 1:
                idx = 1
            new_members[idx].extend(self.members[i])
        
        self.members = new_members
        pass

    def get_best(self):
        for i in range(5, 0, -1):
            if self.members[i].first == None:
                continue
            return self.members[i].get_highest()
        pass


class LinkedList():
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def add(self, member):
        
        if self.first == None:
            self.first = member
            self.last = member

        else:
            self.last.next = member
            self.last = member
        self.size += 1

    def extend(self, linkedList):
        if linkedList.first is None:
            return

        if self.first is None:
            self.first = linkedList.first
            self.last = linkedList.last
            self.size = linkedList.size
        else:
            self.last.next = linkedList.first
            self.last = linkedList.last
            self.size += linkedList.size

        linkedList.first = None
        linkedList.last = None
        linkedList.size = 0
    
    # def extend(self, linkedList):
    #     if linkedList.first == None:
    #         return
        
    #     if self.first == None:
    #         return
        
    #     self.last.next = linkedList.first
    #     self.last = linkedList.last
    #     self.size += linkedList.size

    #     linkedList.first = None
    #     linkedList.last = None
    #     linkedList.size = 0

    def get_highest(self):
        cur = self.first
        result = 0

        while cur:
            if not firedMemberList[cur.id] and version[cur.id] == cur.version:
                result = max(result, cur.id)
            cur = cur.next

        return result

    # def get_highest(self):
    #     if self.first == None:
    #         return -1
    #     result = 0
    #     cur = self.first
    #     for i in range(self.size):
    #         result = max(result, cur.id)

    #         if cur.next == None:
    #             break

    #         cur = cur.next

    #     return result


limit = 100_001
memberList = [None for _ in range(limit)]
firedMemberList = [False] * limit
teamList = [Team() for _ in range(6)]
version = [0] * limit

def init():
    global memberList, firedMemberList, teamList, version
    memberList = [None for _ in range(limit)]
    firedMemberList = [False] * limit
    teamList = [Team() for _ in range(6)]
    version = [0] * limit
    pass

def hire(mID, mTeam, mScore):
    version[mID] += 1
    member = Member(mID, mTeam, mScore, version[mID])

    memberList[mID] = member
    teamList[mTeam].members[mScore].add(member)

    pass

def fire(mID):
    firedMemberList[mID] = True
    pass

def updateSoldier(mID, mScore):
    if firedMemberList[mID]:
        return

    old_member = memberList[mID]
    version[mID] += 1

    new_member = Member(mID, old_member.team, mScore, version[mID])
    memberList[mID] = new_member
    teamList[old_member.team].members[mScore].add(new_member)

# def updateSoldier(mID, mScore):
#     if firedMemberList[mID]:
#         return
#     version[mID] += 1
#     member = memberList[mID]
#     member.version = version[mID]
#     teamList[member.team].members[mScore].add(member)
#     pass

def updateTeam(mTeam, mChangeScore):
    teamList[mTeam].update(mChangeScore)
    pass

def bestSoldier(mTeam):
    return teamList[mTeam].get_best()
    
    pass

# 소스코드와 같은 디렉토리에 input.txt 파일을 생성해서 거기에 입력을 넣은 뒤 아래 주석을 지우면 편하게 실행 가능합니다 :)
fs = open("input.txt", "r")
input = fs.readline

CMD_INIT = 1
CMD_HIRE = 2
CMD_FIRE = 3
CMD_UPDATE_SOLDIER = 4
CMD_UPDATE_TEAM = 5
CMD_BEST_SOLDIER = 6

def run():
    isCorrect = False
    numQuery = int(input())

    for i in range(numQuery):
        line = list(map(int, input().split()))
        cmd = line[0]

        if cmd == CMD_INIT:
            init()
            isCorrect = True
        elif cmd == CMD_HIRE:
            mID, mTeam, mScore = line[1], line[2], line[3]
            hire(mID, mTeam, mScore)
        elif cmd == CMD_FIRE:
            mID = line[1]
            fire(mID)
        elif cmd == CMD_UPDATE_SOLDIER:
            mID, mScore = line[1], line[2]
            updateSoldier(mID, mScore)
        elif cmd == CMD_UPDATE_TEAM:
            mTeam, mChangeScore = line[1], line[2]
            updateTeam(mTeam, mChangeScore)
        elif cmd == CMD_BEST_SOLDIER:
            mTeam = line[1]
            userAns = bestSoldier(mTeam)
            ans = line[2]
            
            # print(userAns, ans)

            if userAns != ans:
                isCorrect = False
        else:
            isCorrect = False

    return isCorrect

T, MARK = map(int, input().split())

for tc in range(1, T + 1):
    score = MARK if run() else 0
    print(f'#{tc} {score}')
