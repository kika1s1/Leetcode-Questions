class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        trust_Table = {}
        checkJudgeTable = {}
        for i, j in trust:
            trust_Table[i] = j
            if i in checkJudgeTable:
                checkJudgeTable[i] = j
            elif j not in trust_Table:
                checkJudgeTable[j] = 0
            else:
                checkJudgeTable[j] = i
        cnt = 0
        value = 0
        for i, j in checkJudgeTable.items():
            if j == 0:
                cnt +=1
                value = i
        if cnt > 1 or cnt == 0:
            return -1
        return value