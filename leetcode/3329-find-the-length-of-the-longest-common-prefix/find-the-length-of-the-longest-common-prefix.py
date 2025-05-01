class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_number = False  

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, number):
        node = self.root
        for digit in str(number):
            if digit not in node.children:
                node.children[digit] = TrieNode()  
            node = node.children[digit]
        node.is_end_of_number = True 
    def search_common_prefix(self, number):
        node = self.root
        cnt = 0  
        for digit in str(number):
            if digit not in node.children:
                break  
            node = node.children[digit]
            cnt += 1  
        return cnt 
class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        trie = Trie()
        for num in arr1:
            trie.insert(num)
        maxim = 0
        for num in arr2:
            maxim = max(trie.search_common_prefix(num), maxim)
        return maxim

