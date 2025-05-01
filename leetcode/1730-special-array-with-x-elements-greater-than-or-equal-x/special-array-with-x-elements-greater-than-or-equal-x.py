class Solution:
    def specialArray(self, nums: List[int]) -> int:
        g_equal = []
        l = len(nums)
        for i in range(l+1):
            val = i
            cnt = 0
            for j in range(l):
                if i <=nums[j]:
                    cnt +=1
            g_equal.append(cnt)
        for i in g_equal:
            val = i
            cnt = 0
            for j in range(l):
                if val <=nums[j]:
                    cnt +=1
            if val ==cnt:
                return val
        return -1


