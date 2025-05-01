class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        #TAMIRAT
        map={}
        
        evens=[]
        res=[]
        for num in nums:
            if num%2==0:
                evens.append(num)
        for num in evens:
            if num not in map:
                map[num]=1
            else:
                map[num] +=1
        if not map : return -1
        maxi = max(map.values())
        for k, v in map.items():
            if v == maxi:
                res.append(k)
        return min(res)