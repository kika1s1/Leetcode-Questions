
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: 
            return []
        ans = []
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level += [node.val]
                for n in node.children: 
                    q.append(n)
            ans.extend([level])
        return ans