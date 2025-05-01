# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: "ListNode") -> List[List[int]]:
        i = 0
        j = 0
        cur_d = 0
        movement = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = [[-1 for _ in range(n)] for _ in range(m)]

        while head is not None:
            res[i][j] = head.val
            newi = i + movement[cur_d][0]
            newj = j + movement[cur_d][1]

            if (
                min(newi, newj) < 0
                or newi >= m
                or newj >= n
                or res[newi][newj] != -1
            ):
                cur_d = (cur_d + 1) % 4
            i += movement[cur_d][0]
            j += movement[cur_d][1]

            head = head.next

        return res