class TrieNode:
    def __init__(self):
        self.children, self.isWord = {}, False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.isWord = True


class Solution:
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.insert(word)

        self.result, self.board = set(), board

        def backtrack(row, col, parent, path):
            letter = self.board[row][col]
            curr_node = parent.children[letter]
            if curr_node.isWord:
                self.result.add(path + letter)
            self.board[row][col] = "#"
            for r, c in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = row + r, col + c
                if (
                    0 <= nr < len(board)
                    and 0 <= nc < len(board[0])
                    and board[nr][nc] in curr_node.children
                ):
                    backtrack(nr, nc, curr_node, path + letter)
            self.board[row][col] = letter
            if not curr_node.children:
                parent.children.pop(letter)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in trie.root.children:
                    backtrack(r, c, trie.root, "")

        return list(self.result)
