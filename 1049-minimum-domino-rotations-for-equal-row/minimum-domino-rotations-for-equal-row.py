class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        top_count = Counter(tops)
        top_big = sorted(top_count.items(), key=lambda x:x[1], reverse=True)[0][0]
        bot_count = Counter(bottoms)
        bot_big = sorted(bot_count.items(), key=lambda x:x[1], reverse=True)[0][0]
        t_count = 0
        b_count = 0
        for a, b in zip(tops, bottoms):
            if a == top_big:
                continue
            elif b == top_big:
                t_count +=1
            else:
                t_count = float("inf")
                break
        for a, b in zip(tops, bottoms):
            if b == bot_big:
                continue
            elif a == bot_big:
                b_count +=1
            else:
                b_count = float("inf")
                break
        
        if min(b_count, t_count) == float("inf"):
            return -1
        else:
            return min(b_count, t_count)
