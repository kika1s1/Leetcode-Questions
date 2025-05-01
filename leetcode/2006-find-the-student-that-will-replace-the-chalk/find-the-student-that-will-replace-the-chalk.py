class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        if len(chalk)  <=1:
            return 0
        tot = sum(chalk)
        k = k%tot
        for i, v in enumerate(chalk):
            if (k-v) < 0:
                return i
            k -=v
        return 0
            