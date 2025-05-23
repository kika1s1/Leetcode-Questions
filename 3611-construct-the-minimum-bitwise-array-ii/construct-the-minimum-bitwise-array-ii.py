class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            found = False
            for i in range(num.bit_length()-1, -1, -1):
                if (num >> i) & 1:
                    x = num ^ (1 << i)  
                    if x | (x + 1) == num:
                        ans.append(x)
                        found = True
                        break
            if not found:
                ans.append(-1)
        return ans
