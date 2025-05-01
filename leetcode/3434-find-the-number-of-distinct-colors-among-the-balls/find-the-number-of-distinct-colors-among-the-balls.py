class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colors = {}
        color_count = {}
        result = []

        for x, y in queries:
            if x in ball_colors:
                prev_color = ball_colors[x]
                color_count[prev_color] -= 1
                if color_count[prev_color] == 0:
                    del color_count[prev_color]

            ball_colors[x] = y
            if y in color_count:
                color_count[y] += 1
            else:
                color_count[y] = 1
            
            result.append(len(color_count))
        
        return result
