class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:

        indices = defaultdict(int)
        totalZero = nums.count(0)
        totalOne = nums.count(1)
        cntZero = 0
        cntOne = 0

        for i in range(len(nums)+1):
            if i == 0:
                if nums[i] == 0:
                    cntZero = 1
                else:
                    cntOne = 1
                indices[i] = totalOne
            elif i == len(nums):
                indices[i] = totalZero
            elif nums[i] == 0:
                indices[i] = cntZero + totalOne-cntOne
                cntZero += 1
            else:
                indices[i] = cntZero + totalOne - cntOne
                cntOne += 1
        ans = []
        maxim = max(indices.values())
        for key, value in indices.items():

            if value == maxim:

                ans.append(key)
        
        return ans
