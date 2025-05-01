class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        c1 = c2 = None
        cnt1 = cnt2 = 0
        for num in nums:
            if num == c1:
                cnt1 += 1
            elif num == c2:
                cnt2 += 1
            elif cnt1 == 0:
                c1, cnt1 = num, 1
            elif cnt2 == 0:
                c2, cnt2 = num, 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        return [x for x in (c1, c2) if nums.count(x) > n // 3]
