class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:

        # indices = defaultdict(int)
        # totalZero = nums.count(0)
        # totalOne = nums.count(1)
        # cntZero = 0
        # cntOne = 0

        # for i in range(len(nums)+1):
        #     if i == 0:
        #         if nums[i] == 0:
        #             cntZero = 1
        #         else:
        #             cntOne = 1
        #         indices[i] = totalOne
        #     elif i == len(nums):
        #         indices[i] = totalZero
        #     elif nums[i] == 0:
        #         indices[i] = cntZero + totalOne-cntOne
        #         cntZero += 1
        #     else:
        #         indices[i] = cntZero + totalOne - cntOne
        #         cntOne += 1
        # ans = []
        # maxim = max(indices.values())
        # for key, value in indices.items():

        #     if value == maxim:

        #         ans.append(key)
        
        # return ans
        l, r = 0, nums.count(1)
        maxScore = r
        maxScoresIndex = [0]

        for i in range(len(nums)):
            if nums[i] == 0:
                l += 1
            else:
                r -= 1
            score = l + r
            if score > maxScore:
                maxScore = score
                maxScoresIndex = [i + 1]
            elif score == maxScore:
                maxScoresIndex.append(i + 1)

        return maxScoresIndex
        