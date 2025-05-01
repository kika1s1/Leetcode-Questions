class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        l = 0
        for num in encoded:
            ans.append(ans[-1] ^ num)
        return ans