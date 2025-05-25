class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        count = 0

        for k in range(1, N + 1):
            if k * (k - 1) // 2 >= N:
                break

            if (N - k * (k - 1) // 2) % k == 0:
                count += 1
        return count
