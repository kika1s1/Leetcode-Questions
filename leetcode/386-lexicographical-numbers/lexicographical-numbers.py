class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        for num in range(1, n+1):
            ans.append(num)
        ans.sort(key=lambda x:str(x))
        return ans