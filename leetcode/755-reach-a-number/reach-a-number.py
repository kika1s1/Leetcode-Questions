class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        step = total = 0

        while total < target:
            step += 1
            total += step
        
        while (total - target) % 2 != 0:
            step += 1
            total += step

        return step
        