class TrieNode:
    def __init__(self):
        self.children = {}
        self.path = [0 for _ in range(26)]
        self.is_end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            node.path[index] += 1
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    def search(self, word):
        cnt= 0
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            cnt += node.path[index]
            if char not in node.children:
                return cnt
            node = node.children[char]
        return cnt
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        ans = []
        for word in words:
            ans.append(trie.search(word))
        return ans
                