class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        al=[]
        ar=[]
        al.append(0)
        c=0
        d=0
        for i in range(len(nums)-1):
            c+=nums[i]
            al.append(c)
        for i in range(-1,-1*len(nums),-1):
            d+=nums[i]
            ar.append(d)
        ar.reverse()
        ar.append(0)
        for i in range(len(ar)):
            ar[i]=abs(ar[i]-al[i])
        return ar
