class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort()
        rep = Counter(arr)
        if arr.count(0) %2 != 0:
            return False
        cnt = 0
        for num in arr:
            
            if num * 2 in rep and num in rep:
                cnt +=2
                rep[num] -=1
                rep[num*2] -=1
                if rep[num] == 0:
                    del rep[num]
                if rep[num*2] == 0:
                    del rep[num*2]
        return cnt == len(arr)