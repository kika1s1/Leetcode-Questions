class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def make_zero(arr, mid):
            pref = [0]*(len(arr)+1)
            for i in range(mid):
                l, r, val = queries[i]
                pref[l] +=val
                pref[r+1] -=val
            for i in range(1, len(arr)):
                pref[i] = pref[i] + pref[i-1]
            for i in range(len(arr)):
                if arr[i] > pref[i]:
                    return False
            return True
        l, r = 0, len(queries)
        best = -1
        while l <=r:
            mid = (l+r)//2
            if make_zero(nums, mid):
                best = mid
                r = mid -1
            else:
                l = mid +1
        return best
            