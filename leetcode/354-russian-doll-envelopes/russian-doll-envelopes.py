
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        heights = [h for _, h in envelopes]
        
        def length_of_lis(seq):
            lis = []
            for x in seq:
                pos = bisect_left(lis, x)
                if pos == len(lis):
                    lis.append(x)
                else:
                    lis[pos] = x
            return len(lis)
        
        return length_of_lis(heights)

