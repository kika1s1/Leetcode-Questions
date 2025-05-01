# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

# @kika1s1
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def backtrack(i, curr, res):
            if i == len(curr):
                res.append(''.join(curr))
                return
            if curr[i].isalpha():
                curr[i] = chr(ord(curr[i]) ^ 32) 
                # this toggle the case lower  tp upper and vs
                backtrack(i + 1, curr, res)
                curr[i] = chr(ord(curr[i]) ^ 32)
                # same with chr(ord(curr[i]) ^ (1 << 5)) 
                # same with curr[i].swapcase()
                
            backtrack(i + 1, curr, res)
        backtrack(0, list(s), res)
        return res