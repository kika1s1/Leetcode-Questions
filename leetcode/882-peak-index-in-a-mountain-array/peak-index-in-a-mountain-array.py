class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1
        while l <=r:
            print
            mid = (l+r)//2
            if arr[mid] > arr[mid-1] and arr[mid+1] < arr[mid]:
                return mid
            elif arr[mid] < arr[mid-1]:
                r = mid
            else:
                l = mid 
        return mid