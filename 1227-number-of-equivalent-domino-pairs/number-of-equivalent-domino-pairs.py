class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt = 0
        domino = defaultdict(int)
        for x, y in dominoes:
            if x > y:
                if (y, x) in domino:
                    cnt +=domino[(y, x)]
                domino[(y, x)] +=1
            else:
                if (x, y) in domino:
                    cnt +=domino[(x, y)]
                domino[(x, y)] +=1
        return cnt