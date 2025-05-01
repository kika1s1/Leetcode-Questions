class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)):
            f = str(nums[i])
            for j in range(i+1, len(nums)):
                s = str(nums[j])
                if gcd(int(f[0]),int(s[-1])) ==1:
                    cnt +=1
                    # print(f, s)
        return cnt