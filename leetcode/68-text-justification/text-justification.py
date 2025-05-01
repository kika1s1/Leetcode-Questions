class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        line = []
        width = 0
        for word in words:
            if width + len(word) + len(line) > maxWidth:
                for i in range(maxWidth - width):
                    line[i % (len(line) - 1 or 1)] += " "
                ans.append("".join(line))
                line, width = [], 0
            line += [word]
            width += len(word)
        ans.append(" ".join(line).ljust(maxWidth))
        return ans
