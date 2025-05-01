class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        rep = Counter(s)
        if len(s) <k:
            return False
        cnt = 0 
        for key,value in rep.items():
            if value%2 ==1:
                cnt +=1
        if cnt >k:
            return False
        return True