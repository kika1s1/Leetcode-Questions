class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        cnt = 1
        prev = None
        for i in range(1, len(nums)):
            if prev is None:
                if nums[i-1] > nums[i]:
                    prev = 1
                    cnt +=1
                elif nums[i-1] == nums[i]:
                    prev = None
                else:
                    prev = -1
                    cnt +=1
            elif prev == -1 and nums[i-1] > nums[i]:
                prev = 1
                cnt +=1
            elif prev == 1 and nums[i-1] < nums[i]:
                prev = -1
                cnt +=1
        return cnt

        # return 1