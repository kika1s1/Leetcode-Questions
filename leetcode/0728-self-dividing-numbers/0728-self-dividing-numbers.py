class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isDivisible(n):
            for i in str(n):
                if i == '0' or int(n) % int(i) != 0:
                    return False
            return True
        ans = []
        for i in range(left, right+1):
            if isDivisible(i):
                ans.append(i)
        return ans

