class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ans = []
        rank_index = {}
        sorted_arr = sorted(arr)
        rank = 0
        prev = None
        for score in sorted_arr:
            if prev == None:
                prev = score
                rank = 1
                rank_index[score] = rank
            elif prev < score:
                rank +=1
                prev = score
                rank_index[score] = rank
            else:
                prev = score
                rank_index[score] = rank
        for point in arr :
            ans.append(rank_index[point])
        return ans
