class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        for i in nums1:
            count=0
            for j in nums2:
                if i==j:
                    for k in range(nums2.index(j)+1,len(nums2)):
                        if nums2[k]>j:
                            count+=1
                            result.append(nums2[k])
                            break
                    if count==0:
                        result.append(-1)
        return result