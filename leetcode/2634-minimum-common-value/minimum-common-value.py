class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        ans = set(nums1) & set(nums2)
        if not ans:
            return -1
        return sorted(list(ans))[0]