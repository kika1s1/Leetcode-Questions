class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        forward = [0]
        backward = [0]
        for index in range(len(nums)):
            forward.append(forward[-1] + nums[index])
            backward.append(backward[-1] + nums[-index-1])
        backward.reverse()
        for index in range(len(nums)):
            if forward[index] == backward[index + 1]:
                return index
        return -1
            