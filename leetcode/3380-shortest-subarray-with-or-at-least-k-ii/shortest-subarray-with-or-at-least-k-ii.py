from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        min_length = float("inf")
        window_start = window_end = 0
        bit_counts = [0] * 32

        while window_end < len(nums):
            self._update_bit_counts(bit_counts, nums[window_end], 1)

            while window_start <= window_end and self._convert_bits_to_num(bit_counts) >= k:
                min_length = min(min_length, window_end - window_start + 1)
                self._update_bit_counts(bit_counts, nums[window_start], -1)
                window_start += 1

            window_end += 1

        return -1 if min_length == float("inf") else min_length

    def _update_bit_counts(self, bit_counts: list, number: int, delta: int) -> None:
        for pos in range(32):
            if number & (1 << pos):
                bit_counts[pos] += delta

    def _convert_bits_to_num(self, bit_counts: list) -> int:
        result = 0
        for pos in range(32):
            if bit_counts[pos]:
                result |= 1 << pos
        return result
