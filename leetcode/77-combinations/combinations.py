class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def helper(i, curr):
            if len(curr) == k:
                ans.append(curr[:])
                return 
            if i > n:
                return
            curr.append(i)
            helper(i+1, curr)
            curr.pop()
            helper(i+1, curr)
        helper(1, [])
        return ans