class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        ans = 0
        for i, j in zip(seats, students):
            ans +=abs(i-j)
        return ans
