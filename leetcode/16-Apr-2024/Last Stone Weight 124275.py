# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)

        while len(stones)  > 1:
            if stones[0] == stones[1]:
                stones.pop(0)
                stones.pop(0)
            else:
                f = stones[0]
                s = stones[1]
                diff = f-s
                stones.append(diff)
                stones.pop(0)
                stones.pop(0)
                stones.sort(reverse=True)
        return stones[0] if stones else 0

        