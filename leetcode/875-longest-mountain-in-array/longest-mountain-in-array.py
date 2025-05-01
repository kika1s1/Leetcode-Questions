class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        maxim = float("-inf")
        got = False
        dec_got = False
        cnt = 1
        for i in range(1, len(arr)):

            if not got and arr[i-1] < arr[i]:
                cnt +=1
                got = True
            elif got and not dec_got and arr[i-1] < arr[i]:
                cnt +=1
            elif got and arr[i-1] > arr[i]:
                cnt +=1
                maxim = max(maxim, cnt)
                dec_got = True
            elif dec_got and arr[i-1] < arr[i]:
                cnt = 2
                dec_got = False
            else:
                cnt = 1
                got = False
                dec_got = False
        return maxim if maxim != float("-inf") else 0

            
