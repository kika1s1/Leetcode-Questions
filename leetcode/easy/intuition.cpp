/*
 * Intuition
 * Platform: LEETCODE
 * Difficulty: easy
 * Language: cpp
 * Problem URL: https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/solutions/6840908/greedy-digits-in-single-loop-without-string-c-py3-beats-100/
 * Date: 2025-06-14T06:49:48.600Z
 * Author: CodeSync Extension
 */

class Solution:    def minMaxDifference(self, num: int) -> int:        decoded = []        while num > 0:            decoded.append(num % 10)            num //= 10        maxim = 0        prev = None        first = decoded[-1]        minim = 0        for index, num in enumerate(decoded[::-1]):            if prev is None and num !=9:                prev = num            if num  == prev:                maxim = (maxim * 10) + 9            else:                maxim = (maxim * 10) + num            if num == first:                minim = minim * 10 + 0            else:                minim = (minim * 10) + num        return maxim - minim