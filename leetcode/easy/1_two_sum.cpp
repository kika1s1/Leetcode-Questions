/*
 * 1. Two Sum
 * Platform: LEETCODE
 * Difficulty: easy
 * Language: cpp
 * Problem URL: https://leetcode.com/problems/two-sum/submissions/
 * Date: 2025-06-11T18:28:59.549Z
 * Author: CodeSync Extension
 */

class Solution:    def twoSum(self, nums: List[int], target: int) -> List[int]:        num_index = {}        for index, num in enumerate(nums):            if target-num in num_index:                return [index, num_index[target-num]]            else:                num_index[num] = index