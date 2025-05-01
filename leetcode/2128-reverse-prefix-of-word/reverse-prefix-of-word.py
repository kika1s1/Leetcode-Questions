class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        curr = []
        for i, char in enumerate(word):
            if char ==ch:
                curr.append(char)
                break
            else:
                curr.append(char)
        if i == len(word)-1 and word[-1] != ch:
            return word
        return "".join(curr[::-1]) + word[i+1:]
