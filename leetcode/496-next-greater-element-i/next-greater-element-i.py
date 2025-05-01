class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = []
        next_great = {}
        for num in nums2:
            if not stack:
                stack.append(num)
            elif stack[-1] >num:
                stack.append(num)
            else:
                while stack and stack[-1] < num:
                    n =  stack.pop()
                    next_great[n] = num
                stack.append(num)
        for num in nums1:
            if num not in next_great:
                ans.append(-1)
            else:
                ans.append(next_great[num])
        return ans
                