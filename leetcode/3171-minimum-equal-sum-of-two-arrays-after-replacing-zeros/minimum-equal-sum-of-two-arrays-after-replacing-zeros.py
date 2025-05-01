class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        cnt10  = nums1.count(0)
        cnt20 = nums2.count(0)
        nums1_sum =  sum(nums1) + cnt10
        nums2_sum =  sum(nums2) + cnt20
        if nums1_sum == nums2_sum:
            return nums2_sum
        elif nums1_sum <= nums2_sum and cnt10 > 0:
            return nums2_sum
        elif nums1_sum >= nums2_sum and cnt20 > 0:
            return nums1_sum
        return -1

