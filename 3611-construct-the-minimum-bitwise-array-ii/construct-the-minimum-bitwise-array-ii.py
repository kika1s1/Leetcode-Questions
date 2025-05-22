class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num & 1 ==0:
                ans.append(-1)
            else:
                cnt = 0
                n = num
                while n & 1 == 1:
                    n >>=1
                    cnt +=1
                ans.append(num -(1<< (cnt-1)))
        return ans

