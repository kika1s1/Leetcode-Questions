class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        a, b = ord(coordinate1[0])-ord("a")+1, int(coordinate1[1])
        x, y = ord(coordinate2[0])-ord("a")+1, int(coordinate2[1])
        if (x+y)%2 == (a+b)%2:
            return True
        return False