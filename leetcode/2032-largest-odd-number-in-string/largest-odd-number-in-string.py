class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        sub = ""
        for i in range(len(num), -1, -1):
            sub = num[0:i]
            if int(num[i-1]) % 2 != 0:
                break
        return sub


