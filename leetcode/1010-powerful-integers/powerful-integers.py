
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans = set()
        
        i = 0
        while x**i <= bound:
            j = 0
            while x**i + y**j <= bound:
                ans.add(x**i + y**j)
                if y == 1:
                    break
                j += 1
            if x == 1:
                break
            i += 1
        
        return list(ans)
