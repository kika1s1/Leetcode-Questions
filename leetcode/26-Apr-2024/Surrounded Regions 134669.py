# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        rows, cols = len(board), len(board[0])
        uf = UnionFind(rows * cols + 1)  # +1 for the virtual node

        virtual_node = rows * cols

        # Connect boundary 'O' cells to the virtual node
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                        uf.union(i * cols + j, virtual_node)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Connect adjacent 'O' cells
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < rows and 0 <= nj < cols and board[ni][nj] == 'O':
                            uf.union(i * cols + j, ni * cols + nj)

        # Flip surrounded 'O' cells to 'X'
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and uf.find(i * cols + j) != uf.find(virtual_node):
                    board[i][j] = 'X'