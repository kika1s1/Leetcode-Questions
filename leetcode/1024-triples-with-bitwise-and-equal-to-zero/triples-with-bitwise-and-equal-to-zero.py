
class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        cnt = 0
        rep = defaultdict(int)
        for i in range(len(nums)):
            for j in range(len(nums)):
                rep[nums[i] & nums[j]] +=1
        for num in nums:
            for digit, times in rep.items():
                if num & digit ==0:
                    cnt += times
        return cnt