class TrieNode:
    def __init__(self):
        self.children = {}
        self.products = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.products.append(word)
            node.products.sort()
            if len(node.products) > 3:
                node.products.pop()
    
    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.products

class Solution:
    def suggestedProducts(self, products, searchWord):
        trie = Trie()
        for product in products:
            trie.insert(product)
        
        prefix = ''
        result = []
        for char in searchWord:
            prefix += char
            suggestions = trie.search(prefix)
            result.append(suggestions)
        return result