class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        even = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even += nums[i]
        for num, index in queries:
            total = nums[index] + num
            if nums[index] % 2 == 0:
                if total % 2 == 0:
                    even +=num
                else:
                    even -= nums[index]
            else:
                if total % 2 == 0:
                    even +=total
            nums[index] = total
            ans.append(even)
        return ans






