class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(p1: List[int], p2: List[int]) -> int:
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        distances = set()
        distances.add(distance(p1, p2))
        distances.add(distance(p1, p3))
        distances.add(distance(p1, p4))
        distances.add(distance(p2, p3))
        distances.add(distance(p2, p4))
        distances.add(distance(p3, p4))

        return len(distances) == 2 and 0 not in distances