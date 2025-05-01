class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        longest_streak = 0

        unique_numbers = set(nums)

        for start_number in nums:
            current_streak = 0
            current = start_number

            while current in unique_numbers:
                current_streak += 1

                if current * current > 10**5:
                    break

                current *= current

            longest_streak = max(longest_streak, current_streak)

        return longest_streak if longest_streak >= 2 else -1