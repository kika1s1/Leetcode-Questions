class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 1000000007

        dp_last: list[list[int]] = [[0 for _ in range(3)] for _ in range(2)]  # previous state
        dp_current: list[list[int]] = [[0 for _ in range(3)] for _ in range(2)]  # current state

        dp_last[0][0] = 1  # empty string

        for _ in range(n):
            for count_a in range(2):
                for count_l in range(3):
                    # choose "P"
                    dp_current[count_a][0] = (dp_current[count_a][0] + dp_last[count_a][count_l]) % MOD
                    # choose "A"
                    if count_a == 0:
                        dp_current[count_a + 1][0] = (dp_current[count_a + 1][0] + dp_last[count_a][count_l]) % MOD
                    # Choose "L"
                    if count_l < 2:
                        dp_current[count_a][count_l + 1] = (
                            dp_current[count_a][count_l + 1] + dp_last[count_a][count_l]
                        ) % MOD

            dp_last = dp_current  # Reference current to previous
            dp_current = [[0 for _ in range(3)] for _ in range(2)]  # make new current

        res: int = sum(dp_last[count_a][count_l] for count_a in range(2) for count_l in range(3)) % MOD
        return res