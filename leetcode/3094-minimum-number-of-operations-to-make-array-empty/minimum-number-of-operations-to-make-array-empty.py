class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mp=defaultdict(int)
        for i in nums:
            mp[i]+=1
        ans=0
        for i in mp.values():
            if i==1:
                return -1
            ans+=(i+2)//3
            
        return ans                

           