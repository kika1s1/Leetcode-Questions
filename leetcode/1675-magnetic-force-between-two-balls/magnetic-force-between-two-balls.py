class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()  
        def can_place_balls(distance):
            count = 1  
            last_position = position[0]
            for i in range(1, len(position)):
                if position[i] - last_position >= distance:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False
        
        left, right = 1, position[-1] - position[0]
        max_distance = 0
        while left <= right:
            mid = (left + right) // 2
            if can_place_balls(mid):
                max_distance = mid
                left = mid + 1
            else:
                right = mid - 1
        return max_distance
