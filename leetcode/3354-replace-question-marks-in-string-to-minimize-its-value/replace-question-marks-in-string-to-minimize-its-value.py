class Solution:
    def minimizeStringValue(self, s: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        rep = defaultdict(int)
        heap = []
        for char in s:
            if char !="?":
                rep[char] +=1
        for char in alphabet:
            if char not in rep:
                heappush(heap, [0, char])
            else:
                heappush(heap, [rep[char], char])
        ans = list(s)
        order = []
        for char in s:
            if char == "?":
                x, a = heappop(heap)
                order.append(a)
                x +=1
                print([x, a])
                heappush(heap, [x, a])
            
        order.sort()
        cnt = 0
        for index, char in enumerate(ans):
            if char == "?":
                ans[index] = order[cnt]
                cnt +=1
        return "".join(ans)
