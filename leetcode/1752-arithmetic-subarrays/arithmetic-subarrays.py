class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def canBeArithmetic(arr):
            if len(arr) < 3:
                return True
            arr.sort()
            d = arr[1] - arr[0]
            for i in range(1, len(arr) - 1):
                if arr[i+1] - arr[i] != d:
                    return False
            return True
        res = []
        for i in range(len(l)):
            a = nums[l[i]:r[i] + 1]
            res.append(canBeArithmetic(a))
        return res