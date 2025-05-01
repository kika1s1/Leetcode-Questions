class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        dist = float("-inf")
        cnt = 0
        ans = 0
        begin = True
        for index, num in enumerate(seats):
            if num == 0:
                cnt +=1
            else:
                if begin:
                    ans = max(ans, cnt)
                cnt = 0
                begin = False
            if ceil(cnt/2) > dist:
                    ans = max(ceil(cnt/2), ans)
        ans = max(ans, cnt)
            
        return ans