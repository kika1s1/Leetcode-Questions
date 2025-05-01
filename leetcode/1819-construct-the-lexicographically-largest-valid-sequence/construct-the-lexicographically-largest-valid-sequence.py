class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0] * (n * 2 - 1)
        used = [False] * (n + 1)
        self.backtrack(0, res, used, n)
        return res

    def backtrack(self, idx, res, used, n):
        if idx == len(res):
            return True

        if res[idx] != 0:
            return self.backtrack(idx + 1, res, used, n)

        for num in range(n, 0, -1):
            if used[num]:
                continue

            used[num] = True
            res[idx] = num

            if num == 1:
                if self.backtrack(idx + 1, res, used, n):
                    return True
            elif idx + num < len(res) and res[idx + num] == 0:
                res[idx + num] = num
                if self.backtrack(idx + 1, res, used, n):
                    return True
                res[idx + num] = 0

            res[idx] = 0
            used[num] = False

        return False
