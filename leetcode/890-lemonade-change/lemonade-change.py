class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change  = defaultdict(int)
        for i in bills:
            if not change and i !=5:
                return False
            elif i == 5:
                change[i] +=1
            elif i == 20:
                if change[10] >=1 and change[5] >=1:
                    change[10] -=1
                    change[5] -=1
                elif change[5]>=3:
                    change[5] -=3
                else:
                    return False
                change[20] +=1
            elif i == 15:
                if change[10]>=1:
                    change[10] -=1
                elif change[5]>=2:
                    change[5] -=2
                else:
                    return False
                change[15] +=1
            elif i == 10:
                if change[5]>=1:
                    change[5] -=1
                else:
                    return False
                change[10] +=1
        return True


        