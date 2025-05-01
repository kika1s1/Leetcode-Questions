class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n !=1 and n not in visited:
            summ = 0
            visited.add(n)
            for i in str(n):
                summ +=int(i)**2
            n = summ
        if n ==1:
            return True
        return False
            