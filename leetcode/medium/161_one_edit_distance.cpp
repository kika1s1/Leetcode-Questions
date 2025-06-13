/*
 * 161. One Edit Distance
 * Platform: LEETCODE
 * Difficulty: medium
 * Language: cpp
 * Problem URL: https://leetcode.com/problems/one-edit-distance/submissions/1486965342/
 * Date: 2025-06-13T07:55:04.122Z
 * Author: CodeSync Extension
 */

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) == len(t) :
            s = sorted(s)
            t = sorted(t)
            if s == t :
                return False
        return True

        if len(s) >= len(t) +2:
            return False
        elif len(s) <= len(t) -2:
            return False
        else:
            return True