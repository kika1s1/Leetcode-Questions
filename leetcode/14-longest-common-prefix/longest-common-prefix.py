class Trie:
    ALPHABET_SIZE = 26
    class TrieNode:
        def __init__(self):
            self.is_end = False
            self.children = [None] * Trie.ALPHABET_SIZE

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            index = ord(c) - ord("a")
            if not curr.children[index]:
                curr.children[index] = self.TrieNode()
            curr = curr.children[index]
        curr.is_end = True
    def InsertAll(self, words, k):
        for k in range(k):
            self.insert(words[k])
    def comman_prefix(self, word):
        curr = self.root
        ans = ""
        for c in word:
            index = ord(c)-ord("a")
            if not curr.children[index] or curr.children.count(None) != 25:
                return ans
            ans +=c
            curr = curr.children[index]
        return ans
    

   

    

class Solution:
    def longestCommonPrefix(self, strs):
        trie = Trie()
        # maxim = float("inf")
        trie.InsertAll(strs, len(strs))
        small = "n"*202
        for word in strs:
            if len(word) < len(small):
                small  = word
        print(small)
        return trie.comman_prefix(small)
