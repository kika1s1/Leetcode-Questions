class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total

        sum_digit_count = defaultdict(list)
        
        maxim = -1

        for num in nums:
            digit_s = digit_sum(num)
            heappush(sum_digit_count[digit_s], num)
            if len(sum_digit_count[digit_s]) > 2:
                heappop(sum_digit_count[digit_s])
            if len(sum_digit_count[digit_s]) == 2:
                maxim = max(maxim, sum(sum_digit_count[digit_s]))

        return maxim
