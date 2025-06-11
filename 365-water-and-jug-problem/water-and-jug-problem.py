class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x + y < target:
            return False
        if x == target or  y == target:
            return True
        return target % (gcd(x, y)) == 0