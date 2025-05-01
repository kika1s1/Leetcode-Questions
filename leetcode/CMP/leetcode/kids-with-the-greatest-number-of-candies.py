class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        aboveAll = max(candies)
        ans = []
        for i in candies:
            if i + extraCandies >= aboveAll:
                ans.append(True)
            else:
                ans.append(False)
        return ans