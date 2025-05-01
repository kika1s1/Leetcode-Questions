class Solution:
    def calculateScore(self, s: str) -> int:
        pos =  defaultdict(list)
        score = 0
        for index, char in enumerate(s):
            if abs(ord(char)-97-25) not in pos:
                pos[ord(char)-97].append(index)
            else:
                value = pos[abs(ord(char)-97-25)].pop()
                score +=index-value
                if len(pos[abs(ord(char)-97-25)]) ==0:
                    del pos[abs(ord(char)-97-25)]
        return score