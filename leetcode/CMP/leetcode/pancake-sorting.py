class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(arr)-1, -1, -1):
            flip = 1 + arr.index(i+1)
            if flip != i+1:
                arr[:flip] = arr[:flip][::-1]
                arr[:i+1] = arr[:i+1][::-1]
                res.append(flip)
                res.append(i+1)
        return res