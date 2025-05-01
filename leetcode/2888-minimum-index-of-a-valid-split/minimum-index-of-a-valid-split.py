class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        f = []
        b = []
        d = defaultdict(int)
        maxim = 0
        for i in range(len(nums)):
            d[nums[i]] +=1
            if d[nums[i]] > (i+1)/2:
                f.append(nums[i])
                maxim = nums[i]
            elif d[maxim] >  (i+1)/2:
                f.append(maxim)
            else:
                f.append(0)
        nums = nums[::-1]
        d = defaultdict(int)
        maxim = 0
        for i in range(len(nums)):
            d[nums[i]] +=1
            if d[nums[i]] > (i+1)/2:
                b.append(nums[i])
                maxim  = nums[i]
            elif d[maxim] >  (i+1)/2:
                b.append(maxim)
            else:
                b.append(0)
        b.reverse()
        for i in range(len(nums)-1):
            if b[i+1] == f[i] and b[i] !=0:
                return i
        return -1
