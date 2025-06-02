class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
      def check(sum1, sum2, nums):
        if len(nums) == 0:
          return sum1 == target and sum2 == target

        return check(sum1 * nums[0], sum2, nums[1::]) or check(sum1, sum2 * nums[0], nums[1::])

      return check(1,1,nums)