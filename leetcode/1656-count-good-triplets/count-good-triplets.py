class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        cnt = 0
        R = len(arr)
        for i in range(R):
            for j in range(i+1, R):
                for k in range(j+1, R):
                    if abs(arr[i] - arr[j]) <=a and abs(arr[j]-arr[k]) <=b and abs(arr[i]-arr[k]) <=c:
                        cnt +=1

        return cnt