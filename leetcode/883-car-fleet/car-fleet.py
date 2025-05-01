class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        spd = {}
        fleet = []
        for i in range(len(position)): 
            spd[position[i]] = speed[i]

        position.sort()

        for p in position[::-1]: #traverse in reverse
            time = (target-p)/spd[p] #track the current car's time to reach the goal
            if p == position[-1] or time > fleet[-1]: #if the current car requires more time than the last car, it turns into its own fleet
                fleet.append(time)

        return len(fleet)