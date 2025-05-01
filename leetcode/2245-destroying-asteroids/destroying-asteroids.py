class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        back = [mass]
        for i in range(len(asteroids)-1):
            if back[-1] + asteroids[i] > asteroids[i+1]:
                back.append(back[-1] + asteroids[i])
            else:
                return False
        return True


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        
        for asteroid in asteroids:
            if mass < asteroid:
                return False
            mass = mass + asteroid
        
        return True