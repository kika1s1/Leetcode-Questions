class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        repeated = {}
        cnt = 0
        prev = 0
        maxim = 0
        for i in range(len(s)):
            char = s[i]
            if char in repeated:
                repeated[char] += 1
            else:
                repeated[char] = 1
            cnt += 1
            while repeated[char] > 2:
                repeated[s[prev]] -= 1
                cnt -= 1
                prev += 1
            maxim = max(maxim, cnt)
        return maxim
