from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        table = defaultdict(int)
        table[k] = 1
        nice_subarray = 0
        for num in nums:
            if num%2==1:
                 count+=1
            nice_subarray += table[count]
            table[k+count] += 1

        return nice_subarray