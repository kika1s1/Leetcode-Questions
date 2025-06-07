class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        prefix = [0]
        N = len(nums)
        def find_sum(target, l, r):
            r -=1
            while l <= r:
                mid = (l+r)//2
                if prefix[mid] == target:
                    return True, N-mid
                elif prefix[mid] > target:
                    # r = mid +1
                    r = mid-1
                else:
                    l = mid+1
            return False, float("inf")


        for num in nums:
            prefix.append(prefix[-1] + num)
        ans = float("inf")
        for index, pref in enumerate(prefix):
            if pref == x:
                ans = min(ans, index)
            is_found, maxim = find_sum(prefix[-1]- (x-pref), index+1, N)
            if is_found:
                ans = min(ans, maxim + index)
        if ans ==float("inf"):
            return -1
        return ans

