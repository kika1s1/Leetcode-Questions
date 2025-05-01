class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s,n=set(nums),len(nums)
        for i in range(1,n+1):
            if i not in s:
                t=i
                break
        s1=sum(nums)
        s2=(n*(n+1))//2
        d=s2-s1
        return t-d,t