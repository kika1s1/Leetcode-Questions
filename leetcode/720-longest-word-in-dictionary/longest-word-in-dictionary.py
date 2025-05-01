class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None] * 26
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            index = ord(char)- ord("a")
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.is_end = True
        
    def insertAll(self, arr):
        for word in arr:
            self.insert(word)

    def returnLongest(self):
        root = self.root
        def dfs(root):
            ans = []
            for i in range(len(root.children)):
                if root.children[i] and root.children[i].is_end:
                    char = chr(97 + i)
                    current = [char]

                    current.extend(dfs(root.children[i]))
                    if len(current) > len(ans):
                        ans = current
            return ans


        ans = dfs(root)
        return "".join(ans)
        
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        trie.insertAll(words)
        return trie.returnLongest()
        
        