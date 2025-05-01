class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        move = 0
        while maxDoubles > 0 and target > 1:
            if target % 2 != 0:
                target -= 1
                move += 1
            else:
                target //= 2
                move += 1
                maxDoubles -= 1
        return move + target - 1