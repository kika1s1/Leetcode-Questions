class Solution:
    def numTeams(self, rating: List[int]) -> int:
        total = 0
        n = len(rating)
        
        for i in range(n):
            right_less = 0
            right_more = 0
            left_less = 0
            left_more = 0

            for j in range(i + 1, n):
                if rating[j] < rating[i]:
                    right_less += 1
                elif rating[j] > rating[i]:
                    right_more += 1
            
            for j in range(i):
                if rating[j] < rating[i]:
                    left_less += 1
                elif rating[j] > rating[i]:
                    left_more += 1

            total += right_less * left_more + right_more * left_less

        return total