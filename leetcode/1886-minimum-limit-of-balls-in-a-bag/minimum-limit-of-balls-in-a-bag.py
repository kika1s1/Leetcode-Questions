class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def possible(arr, k, value):
            cnt = 0
            for num in arr:
                if num > value:
                    cnt += (ceil(num/value) - 1)
            return cnt <=k
        l, r = 1, max(nums)
        best = float("inf")
        while l <=r:
            mid = (l+r)//2
            if possible(nums[:], maxOperations, mid):
                best = mid
                r = mid -1
            else:
                l = mid +1
        return best
