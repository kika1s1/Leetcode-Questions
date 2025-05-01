class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        s, p, c = 0, -1, capacity
        for idx, plant in enumerate(plants):
            if plant <= c: 
                s += idx - p
                c -= plant
            else:
                s += p + idx + 2
                c = capacity - plant
            p = idx
        return s