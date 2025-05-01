class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        c = Counter(arr1)
        res = []       
        for i in arr2:
            res += [i]*c.pop(i)  
        return res + sorted(c.elements())