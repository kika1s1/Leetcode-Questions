class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone_map = {
                    '2': 'abc',
                    '3': 'def',
                    '4': 'ghi',
                    '5': 'jkl',
                    '6': 'mno',
                    '7': 'pqrs',
                    '8': 'tuv',
                    '9': 'wxyz'
                }
        result = []
        def backtrack(cand, index):
            if len(cand) == len(digits):
                result.append("".join(cand))
                return
            for i in range(len(phone_map[digits[index]])):
                cand.append(phone_map[digits[index]][i])
                backtrack(cand, index+1)
                cand.pop()


        backtrack([], 0)
        return result


