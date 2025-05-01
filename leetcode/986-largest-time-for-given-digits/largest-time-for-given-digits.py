class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        max_time = -1
        best_time = ""

        for perm in permutations(arr):
            h1, h2, m1, m2 = perm
            hours = h1 * 10 + h2
            minutes = m1 * 10 + m2

            if 0 <= hours < 24 and 0 <= minutes < 60:
                current_time = hours * 60 + minutes  
                if current_time > max_time:
                    max_time = current_time
                    best_time = f"{h1}{h2}:{m1}{m2}"

        return best_time if best_time else ""
