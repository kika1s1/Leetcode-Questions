class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        old = score
        prev = score
        b = sorted(score, reverse=True)
        count = 0
        for i in b:
            if count < len(rank):
                prev[prev.index(i)] = rank[count]
                count += 1
            else:
                prev[prev.index(i)] = str(count+1)
                count += 1
        return prev