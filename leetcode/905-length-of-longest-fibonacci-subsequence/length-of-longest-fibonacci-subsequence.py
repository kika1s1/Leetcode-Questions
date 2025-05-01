class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        num_set = set(arr)
        maxim = 0
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                prev = arr[j]
                curr = arr[i] + arr[j]
                cnt = 2
                while curr in num_set:
                    prev, curr = curr, curr + prev
                    cnt += 1
                    maxim = max(maxim, cnt)
        return maxim  