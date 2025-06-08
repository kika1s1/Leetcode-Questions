class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        index = None
        N = len(nums)
        heap =  []
        heappush(heap, (nums[-1], len(nums)-1))
        for i in range(N-2, -1, -1):
            if nums[i+1] > nums[i]:
                ind =  i+1
                index = i+1
                while heap:
                    x, j = heappop(heap)
                    if abs(x) >nums[i] and nums[i+1] > abs(x):
                        ind = j
                        break
                nums[i],  nums[ind] = nums[ind], nums[i]
                break
            else:
                heappush(heap, (nums[i], i))
        if index == None:
            return nums.reverse()
        nums[:] = nums[:index] + sorted(nums[index:])


