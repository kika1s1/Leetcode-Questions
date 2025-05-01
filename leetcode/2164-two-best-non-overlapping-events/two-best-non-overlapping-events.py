class Solution:
    def maxTwoEvents(self, events):
        times = []
        for e in events:
            times.append([e[0], 1, e[2]])
            times.append([e[1] + 1, 0, e[2]])

        ans, max_value = 0, 0
        times.sort()

        for time_value in times:
            if time_value[1]:
                ans = max(ans, time_value[2] + max_value)
            else:
                max_value = max(max_value, time_value[2])

        return ans