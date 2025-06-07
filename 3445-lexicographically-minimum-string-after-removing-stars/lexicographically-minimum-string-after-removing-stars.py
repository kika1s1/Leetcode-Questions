class Solution:
    def clearStars(self, s: str) -> str:
        marked_deleted = set()
        heap = []
        for index, char in enumerate(s):
            if char == "*":
                chr, ind =  heappop(heap)
                marked_deleted.add(-ind)
            else:
                heappush(heap, (char, -index))
        ans = []
        for index, char in enumerate(s):
            if char !="*" and index not in marked_deleted:
                ans.append(char)
        return "".join(ans)