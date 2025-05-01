# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]
class Trie:


    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = ord(c)- ord("a")
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.is_end = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            index = ord(c)-ord("a")
            if not curr.children[index]:
                return False
            else:
                curr = curr.children[index]
        return True if curr.is_end else False


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            index = ord(c)-ord("a")
            if not curr.children[index]:
                return False
            else:
                curr = curr.children[index]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)