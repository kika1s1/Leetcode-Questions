class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # result = set()
        # current = set()

        # for num in arr:
        #     current = {x | num for x in current} | {num}
        #     result |= current

        # return len(result)
        result = set()
        current = set()
        for num in arr:
            temp = set()
            for x in current:
                temp.add(x | num)
            temp.add(num)
            current = temp
            result |= temp

        return len(result)