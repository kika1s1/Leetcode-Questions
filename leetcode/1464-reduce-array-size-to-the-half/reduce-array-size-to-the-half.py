class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        total = len(arr)
        rep = Counter(arr)
        half =  total//2
        sorted_rep = sorted([(x, y) for x, y in rep.items()], key=lambda x:x[1], reverse=True)
        for index, (a, b) in enumerate(sorted_rep):
            total -=b
            if total <=half:
                return index+1

        return 1
