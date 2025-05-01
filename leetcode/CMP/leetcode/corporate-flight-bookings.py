class Solution:
    def corpFlightBookings(self, bookings, n: int):
        ans = [0]*(n+1)
        for i,j,k in bookings:
            ans[i-1] += k
            ans[j]   -= k
        ans.pop()
        prev = ans[0]
        for i in range(1,n):
            prev = ans[i] = prev + ans[i]
        return ans