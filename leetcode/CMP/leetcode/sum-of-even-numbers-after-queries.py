class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s = 0
        for i in nums:
            s += i if i % 2 == 0 else 0
        ans = []
        for q in queries:
            if nums[q[1]] % 2 == 0:
                s -= nums[q[1]]
            nums[q[1]] += q[0]
            if nums[q[1]] % 2 == 0:
                s += nums[q[1]]
            ans.append(s)
        return ans