class Solution:
    def findDuplicates(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(len(arr)):
            index = abs(arr[i])
            if arr[index-1] < 0:
                res.append(abs(arr[i]))
            else:
                arr[index-1] = -arr[index-1]
        return res