class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        weekends = 0
        latest_end = 0

        meetings.sort()

        for start, end in meetings:
            if start > latest_end + 1:
                weekends += start - latest_end - 1

            latest_end = max(latest_end, end)

        weekends += days - latest_end

        return weekends