class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: 
            return False
        if arr[1] <= arr[0]: 
            return False
        i = 1
        while i < len(arr) and arr[i] > arr[i-1]:
            i += 1
        if i == len(arr) or arr[i] == arr[i-1]: 
            return False
        while i < len(arr) and arr[i] < arr[i-1]:
            i += 1
        if i == len(arr): 
            return True
        return False