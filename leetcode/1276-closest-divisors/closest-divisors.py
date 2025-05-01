class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        ans1 = []
        x = num+1
        mid = int(sqrt(x))
        for i in range(mid, -1, -1):
            if x % i == 0:
                ans1 = [i, x//i]
                break
        ans2 = []
        x = num+2
        mid = int(sqrt(x)) 
        for i in range(mid, -1, -1):
            if x % i == 0:
                ans2 = [i, x//i]
                break
        x, y = ans1
        a, b = ans2
        if abs(x-y) > abs(a-b):
            return ans2
        return ans1
