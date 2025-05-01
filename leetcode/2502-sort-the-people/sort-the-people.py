class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        N = len(names)
        for i in range(N):
            max_i = i
            for j in range(i+1, N):
                if heights[j] > heights[max_i]:
                    max_i = j
            names[i], names[max_i] = names[max_i], names[i]
            heights[i], heights[max_i] = heights[max_i], heights[i]
        return names