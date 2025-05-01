class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        ans = []
        max_value, acc_sum = 0, 0
        for num in nums:
            max_value = max(max_value, num)
            acc_sum += num + max_value
            ans.append(acc_sum)

        return ans
        