class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        memo = {}
        
        def dfs(index):
            if index in memo:
                return memo[index]
            if index == len(s):
                return True
            
            node = trie.root
            for i in range(index, len(s)):
                if s[i] not in node.children:
                    break
                node = node.children[s[i]]
                if node.is_end_of_word and dfs(i + 1):
                    memo[index] = True
                    return True
            
            memo[index] = False
            return False
        
        return dfs(0)