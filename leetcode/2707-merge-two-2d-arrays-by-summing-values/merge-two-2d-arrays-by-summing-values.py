class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []
        l, r = 0, 0
        while r < len(nums2) and l < len(nums1):
            un_id_l, value_l = nums1[l]
            un_id_r, value_r= nums2[r]
            if un_id_l == un_id_r:
                ans.append([un_id_r, value_l + value_r])
                l +=1
                r +=1
            elif un_id_l > un_id_r:
                ans.append([un_id_r, value_r])
                r +=1
            else:
                ans.append([un_id_l, value_l])
                l +=1
        while l < len(nums1):
            un_id_l, value_l = nums1[l]
            ans.append([un_id_l, value_l])
            l += 1
        while r < len(nums2):
            un_id_r, value_r = nums2[r]
            ans.append([un_id_r, value_r])
            r +=1
        return ans



