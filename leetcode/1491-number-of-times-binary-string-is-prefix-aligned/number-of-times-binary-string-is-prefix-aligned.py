class Solution(object):
    def numTimesAllBlue(self, flips):
        """
        :type flips: List[int]
        :rtype: int
        """
        right = moves = 0
        for i, f in enumerate(flips, 1):
            right = max(right, f)
            moves = (right == i) + moves
            print(moves)
        return moves