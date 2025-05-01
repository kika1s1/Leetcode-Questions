class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1=-1000
        m2=-1000
        m3=-1000
        for i in nums:
            if i>=m1:
                m3=m2
                m2=m1
                m1=i
            elif i>=m2:
                m3=m2
                m2=i
            elif i>m3:
                m3=i
        temp1=m1*m2*m3
        
        l1=1000
        l2=1000
        
        for i in nums:
            if i<=l1:
                l2=l1
                l1=i
            elif i<l2:
                l2=i
        temp2=l1*l2
        return max(temp1,temp2*m1)