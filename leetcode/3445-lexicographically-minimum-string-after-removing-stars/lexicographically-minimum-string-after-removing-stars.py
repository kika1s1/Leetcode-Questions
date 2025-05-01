class Solution:
    def clearStars(self, s: str) -> str:
        ls = list(s)
        heap = []
        for i, j in enumerate(ls):
            if j == "*":
                val, index = heappop(heap)
                ls[-index] = ""
                ls[i] = ""
            else:
                heappush(heap, (j, -i))
        # ans = ""
        print(ls)
        return "".join(ls)


