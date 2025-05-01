class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        runSum = sum(arr[:k-1])
        l = 0
        for r in range(k-1, len(arr)):
            runSum += arr[r]
            if runSum//k >= threshold:
                res += 1
            runSum -= arr[l]
            l+=1
        return res