class Solution:
    def rotateTheBox(self, box):
        m, n = len(box), len(box[0])
        result = [["."] * m for _ in range(n)]

        for i in range(m):
            falling_stone = n - 1
            for j in range(n - 1, -1, -1):
                if box[i][j] == "#":
                    box[i][j], box[i][falling_stone] = ".", "#"
                    falling_stone -= 1
                elif box[i][j] == "*":
                    falling_stone = j - 1

        for i in range(m):
            for j in range(n):
                result[j][m - i - 1] = box[i][j]

        return result
