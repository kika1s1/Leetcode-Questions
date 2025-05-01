class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare_nums(num1, num2):
            if num1 + num2 < num2 + num1:
                return 1
            elif num1 + num2 > num2 + num1:
                return -1
            else:
                return 0
        arr = [str(num) for num in nums]

        arr.sort(key=cmp_to_key(compare_nums))
        if list(set(arr)) ==['0']:
            return "0"
        return (''.join(arr))