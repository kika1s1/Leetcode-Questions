class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = []

        for i in range(0, len(s), k):
            w = s[i: i+k]

            if len(result) % 2 == 0:
                w = w[::-1]
            
            result.append(w)

        return ''.join(result)
        