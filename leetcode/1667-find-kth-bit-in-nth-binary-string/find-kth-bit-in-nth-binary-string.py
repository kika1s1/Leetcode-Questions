class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def revInvert(data):
            reverse = data[::-1]
            ans = ""
            for i in reverse:
                if i =="0":
                    ans +="1"
                else:
                    ans +="0"
            return ans
        simulate = "0"
        for i in range(1,n+1):
            simulate += "1" + revInvert(simulate)
        return simulate[k-1]