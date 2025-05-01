class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1 
        ans = 0
        prefix_sum = 0
        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 0:
                ans += odd_count 
                even_count += 1
            else:
                ans += even_count
                odd_count += 1
            ans %= MOD 
        return ans
