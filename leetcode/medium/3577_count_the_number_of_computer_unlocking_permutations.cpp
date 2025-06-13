/*
 * 3577. Count the Number of Computer Unlocking Permutations
 * Platform: LEETCODE
 * Difficulty: medium
 * Language: cpp
 * Problem URL: https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/
 * Date: 2025-06-13T12:06:20.308Z
 * Author: CodeSync Extension
 */

class Solution:    def countPermutations(self, complexity: List[int]) -> int:        if complexity.count((complexity)) > 1:            return 0        return factorial(len(complexity)-1)