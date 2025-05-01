class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        visited = set()
        N  = len(nums)
        for i in range(N-1, -1, -1):
            print(i)
            if nums[i] not in visited:
                visited.add(nums[i])
            else:
                break
        else:
            return 0
        return ceil((i+1)/3)