class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        numberOfMove = 0
        while maxDoubles > 0 and target > 1:
            if target % 2 != 0:
                target -= 1
                numberOfMove += 1
            else:
                target //= 2
                numberOfMove += 1
                maxDoubles -= 1
        return numberOfMove + target - 1