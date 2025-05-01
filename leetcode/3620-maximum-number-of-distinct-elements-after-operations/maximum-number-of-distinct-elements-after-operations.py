class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        minim = nums[0]-k
        cnt = 1
        for index, num in enumerate(nums[1:], start=1):
            if num-k > minim:
                minim = num-k
                cnt +=1
            elif -k <= num - minim-1 <=k:
                minim +=1
                cnt +=1
        return cnt