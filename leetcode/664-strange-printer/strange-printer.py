class Solution:
    def strangePrinter(self, s: str) -> int:
        s = "".join(char for char, _ in itertools.groupby(s))
        n = len(s)

        min_turns = [[0] * n for _ in range(n)]

        for i in range(n):
            min_turns[i][i] = 1

        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1

                min_turns[start][end] = length

                for split in range(length - 1):
                    total_turns = (
                        min_turns[start][start + split]
                        + min_turns[start + split + 1][end]
                    )

                    if s[start + split] == s[end]:
                        total_turns -= 1

                    min_turns[start][end] = min(
                        min_turns[start][end], total_turns
                    )

        return min_turns[0][n - 1] if n > 0 else 0