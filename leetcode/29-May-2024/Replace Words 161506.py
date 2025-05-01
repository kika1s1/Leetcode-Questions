# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None]*26

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for chr in word:
            index = ord(chr)-ord("a")
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.is_end = True
    
    def returnSmall(self, word):
        ans = ""
        curr = self.root
        for char in word:
            index = ord(char)-ord("a")
            if not curr.children[index]:
                break
            curr = curr.children[index]
            ans += char
            if curr.is_end:
                return ans
        return word 


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        tr = Trie()
        for name in dictionary:
            tr.insert(name)
        words = sentence.split(" ")
        pos = []
        for w in words:
            pos.append(tr.returnSmall(w))
        return " ".join(pos)
