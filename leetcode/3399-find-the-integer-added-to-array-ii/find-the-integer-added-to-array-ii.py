class Solution:
    def minimumAddedInteger(self, nums1, nums2):
        n = len(nums1)

        min1_1, min1_2, min1_3 = float('inf'), float('inf'), float('inf')
        for val in nums1:
            if val < min1_1:
                min1_3 = min1_2
                min1_2 = min1_1
                min1_1 = val
            elif val < min1_2:
                min1_3 = min1_2
                min1_2 = val
            elif val < min1_3:
                min1_3 = val

        min2 = float('inf')
        for val in nums2:
            min2 = min(min2, val)

        candidates = [min2 - min1_1, min2 - min1_2, min2 - min1_3]

        numberOccurs = [0] * 1001
        for i in range(n):
            n1 = nums1[i]
            numberOccurs[n1] += 1

        minX = float('inf')
        for possibleX in candidates:
            numberCounts = [0] * 1001
            isPossible = True
            for i in range(n - 2):
                target = nums2[i] - possibleX
                if target < 0 or target > 1000 or numberOccurs[target] == 0 or numberCounts[target] == numberOccurs[target]:
                    isPossible = False
                    break
                else:
                    numberCounts[target] += 1

            if isPossible:
                minX = min(minX, possibleX)

        return minX