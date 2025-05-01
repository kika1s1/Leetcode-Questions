# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
  def findMaximumXOR(self, nums: List[int]) -> int:
    maxNum = max(nums)
    if maxNum == 0:
      return 0
    maxBit = int(math.log2(maxNum))
    ans = 0
    mask = 0
    for i in range(maxBit, -1, -1):
      mask |= 1 << i
      prefixes = set([num & mask for num in nums])
      candidate = ans | 1 << i
      for prefix in prefixes:
        if prefix ^ candidate in prefixes:
          ans = candidate
          break

    return ans