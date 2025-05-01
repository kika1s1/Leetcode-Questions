class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct = [nums[0]]
        for i in range(1, len(nums)):
            leftProduct.append(leftProduct[i-1]*nums[i])
        nums.reverse()
        rightProduct = [nums[0]]
        for i in range(1, len(nums)):
            rightProduct.append(rightProduct[i-1]*nums[i])
        rightProduct.reverse()
        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(rightProduct[i+1])
            elif i == len(nums)-1:
                ans.append(leftProduct[i-1])
            else:
                ans.append(leftProduct[i-1] * rightProduct[i+1])
        return ans
