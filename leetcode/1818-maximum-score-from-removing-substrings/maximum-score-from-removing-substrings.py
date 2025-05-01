class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        total = 0

        first_pair = "ab" if x > y else "ba"
        second_pair = "ba" if x > y else "ab"
        first_value = max(x, y)
        second_value = min(x, y)

        def remove_pairs(s, pair, value):
            stack = []
            count = 0
            for char in s:
                if stack and stack[-1] == pair[0] and char == pair[1]:
                    stack.pop()
                    count += value
                else:
                    stack.append(char)
            return ''.join(stack), count

        s, count1 = remove_pairs(s, first_pair, first_value)
        total += count1

        s, count2 = remove_pairs(s, second_pair, second_value)
        total += count2

        return total
