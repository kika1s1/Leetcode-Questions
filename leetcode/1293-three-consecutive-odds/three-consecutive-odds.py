class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for num in arr:
            if cnt >=3:
                return True
            elif num%2 == 1:
                cnt +=1
            else:
                cnt = 0
        return True if cnt >=3 else False