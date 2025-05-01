class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefXOR = [0] *(len(arr)+1)
        xor = arr[0]
        for i in range(len(arr)):
            prefXOR[i+1] = prefXOR[i]^arr[i]
        ans = []
        for i, j in queries:
            ans.append(prefXOR[j+1] ^ prefXOR[i])
        return ans
