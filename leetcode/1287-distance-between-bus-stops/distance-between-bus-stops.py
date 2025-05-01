class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start == destination:
            return 0
        elif start < destination:
            trip = sum(distance[start:destination])
        else:
            trip = sum(distance[destination:start])

        circle = sum(distance)

        if circle - trip > trip:
            return trip
        return circle - trip