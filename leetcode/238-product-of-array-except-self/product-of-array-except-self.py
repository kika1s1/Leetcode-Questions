class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(prefix[-1] * nums[i])
        for i in range(len(nums)-1,-1, -1):
            if i == len(nums)-1:
                postfix.append(nums[i])
            else:
                postfix.append(postfix[-1] * nums[i])
        postfix = postfix[::-1]
        print(prefix)
        print(postfix)
        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(postfix[i+1])
            elif i == len(nums)-1:
                ans.append(prefix[i-1])
            else:
                ans.append(prefix[i-1] * postfix[i+1])
        return ans
        