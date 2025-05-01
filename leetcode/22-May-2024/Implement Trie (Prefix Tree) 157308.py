# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie:

    def __init__(self):
        self.root = {}

        
        

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if not w in cur:
                cur[w] = {}
            cur = cur[w]
        cur['*'] = ''

        

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if not w in cur:
                return False
            cur = cur[w]
        return True if '*' in cur else False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            if not w in cur:
                return False
            cur = cur[w]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)