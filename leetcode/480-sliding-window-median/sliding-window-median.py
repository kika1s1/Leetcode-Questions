from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = SortedList()
        ans = []
        for i in range(len(nums)):
            window.add(nums[i])
            if i >= k:
                window.remove(nums[i - k])
            if i >= k - 1:
                if k % 2 == 0:
                    ans.append((window[k // 2 - 1] + window[k // 2]) / 2)
                else:
                    ans.append(window[k // 2])
        return ans
