class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        cnt = 0
        for i in range(len(arr1)):
            is_true = True
            for j in range(len(arr2)):
                if abs( arr1[i] - arr2[j]) <= d:
                    is_true = False
                    break
            if  is_true:
                cnt +=1
        return cnt

