class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p = m + n
        while 0 < m and 0 < n:
            if nums1[m-1] >= nums2[n-1]:
                nums1[p-1] = nums1[m-1]
                m -= 1
            else:
                nums1[p-1] = nums2[n-1]
                n -= 1
            p -= 1
        while 0 < n:
            nums1[p-1] = nums2[n-1]
            p -= 1; n -= 1