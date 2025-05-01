# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        word_bits = []
        for word in words:
            bits = 0
            for char in word:
                bits |= 1 << (ord(char) - ord('a'))
            word_bits.append(bits)
        
        maxim = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if word_bits[i] & word_bits[j] == 0:
                    maxim = max(maxim, len(words[i]) * len(words[j]))
        
        return maxim