class Solution:
    def trap(self, height: List[int]) -> int:
        indexMax = 0
        listLen = len(height)
        total = 0
        for i in range(1,listLen):
            if height[i] > height[indexMax]:
                indexMax = i
        nowMax = height[0]
        for i in range(1, indexMax):
            if height[i] > nowMax:
                nowMax = height[i]
            else:
                total += (nowMax-height[i])
        nowMax = height[listLen-1]
        for i in range(listLen-1, indexMax, -1):
            if height[i] > nowMax:
                nowMax = height[i]
            else:
                total += (nowMax-height[i])
        return total