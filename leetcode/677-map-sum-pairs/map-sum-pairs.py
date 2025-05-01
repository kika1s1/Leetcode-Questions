class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.value = 0

class MapSum:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for char in key:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True
        curr.value = val

    def sum(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return self._dfs(curr)

    def _dfs(self, node: TrieNode) -> int:
        total = node.value
        for child in node.children.values():
            total += self._dfs(child)
        return total




# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)