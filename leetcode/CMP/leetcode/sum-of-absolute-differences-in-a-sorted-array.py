class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        sm,pr=sum(nums),0
        for i in range(len(nums)):
            pr+=nums[i]
            nums[i]=(((i+1)*nums[i]-pr)+(sm-pr)-(len(nums)-i-1)*nums[i])
        return nums