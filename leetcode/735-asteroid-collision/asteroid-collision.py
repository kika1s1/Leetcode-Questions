class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
            else:
                is_the_same = False
                while stack and stack[-1] > 0  and  asteroid < 0:
                    value = stack.pop()
                    if abs(value) == abs(asteroid):
                        is_the_same = True
                        break
                    else:
                        if abs(value) > abs(asteroid):
                            asteroid =  value
                if not is_the_same:
                    stack.append(asteroid)
        return stack