/*
 * Water And Jug Problem
 * Platform: LEETCODE
 * Difficulty: medium
 * Language: cpp
 * Problem URL: https://leetcode.com/problems/water-and-jug-problem/submissions/1661138452/
 * Date: 2025-06-11T18:23:20.557Z
 * Author: CodeSync Extension
 */

class Solution:    def canMeasureWater(self, x: int, y: int, target: int) -> bool:        if x + y < target:            return False        if x == target or  y == target:            return True        return target % (gcd(x, y)) == 0