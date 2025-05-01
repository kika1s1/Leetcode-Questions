from collections import defaultdict
class Solution:
    def numberOfPairs(self, nums1, nums2, k):
        count_nums2 = defaultdict(int)
        for num in nums2:
            count_nums2[num * k] += 1
        good_pairs = 0

        for num in nums1:
            for i in range(1, int(num ** 0.5) + 1):
                if num % i == 0:
                    if i in count_nums2:
                        good_pairs += count_nums2[i]
                    
                    if i != num // i and num // i in count_nums2:
                        good_pairs += count_nums2[num // i]
        
        return good_pairs