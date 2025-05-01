class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res=[]
        num=0
        for i in nums:
            num=(num*2+i)%5
            res.append(num==0)
        return res