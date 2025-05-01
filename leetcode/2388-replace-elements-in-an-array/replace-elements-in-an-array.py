class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        mp = {}

        for i in range(len(nums)):
            mp[nums[i]] = i
        for i, j in operations:
            current, newEl = i, j
            nums[mp[current]] = newEl
            mp[newEl] = mp[current]

        return nums