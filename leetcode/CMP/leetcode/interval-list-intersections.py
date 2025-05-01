from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        top, bot = 0, 0
        ans = []

        while top < len(firstList) and bot < len(secondList):
            f_start, f_end = firstList[top]
            s_start, s_end = secondList[bot]

            if s_start <= f_end and s_end >= f_start:
                ans.append([max(s_start, f_start), min(s_end, f_end)])

            if f_end < s_end:
                top += 1
            else:
                bot += 1

        return ans
