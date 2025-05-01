class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        numCounter = dict(Counter(arr))
        minPercent = 25
        totalRepatation = len(arr)
        for key, value in numCounter.items():
            if (value/totalRepatation)*100 > minPercent:
                return key
        