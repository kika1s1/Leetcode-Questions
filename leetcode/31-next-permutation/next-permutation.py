class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        index=-1
        n=len(arr)
        for i in range(n-2,-1,-1):
            if arr[i]<arr[i+1]:
                index=i
                break
        if index==-1:
            arr[:]=arr[::-1]
            return arr
        for i in range(n-1,index-1,-1):
            if arr[index]<arr[i]:
                arr[index],arr[i]=arr[i],arr[index]
                break
        arr[::]=arr[:index+1]+sorted(arr[index+1:])
        return arr 