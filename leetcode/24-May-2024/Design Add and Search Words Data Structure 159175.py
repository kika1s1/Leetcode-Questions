# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for chr in word:
            index = ord(chr) - ord("a")
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.is_end = True

    def search(self, word: str) -> bool:
        return self._search_in_node(word, self.root)

    def _search_in_node(self, word: str, node: TrieNode) -> bool:
        curr = node
        for i, c in enumerate(word):
            if c != ".":
                index = ord(c) - ord("a")
                if not curr.children[index]:
                    return False
                curr = curr.children[index]
            else:
                for child in curr.children:
                    if child and self._search_in_node(word[i + 1:], child):
                        return True
                return False
        return curr.is_end

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
