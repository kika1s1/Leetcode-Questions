class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        nums = list(s)
        new_nums = []
        for i in nums:
            if i == "1":
                new_nums.insert(0, i)
            else:
                new_nums.append("0")
        if int(("".join(new_nums)),2) % 2 ==1:
            return "".join(new_nums)
        for i in range(len(new_nums)-1):
            while i < len(nums)-1 and   new_nums[i] == "1" and  new_nums[i+1] =="0":
                new_nums[i], new_nums[i+1] = new_nums[i+1], new_nums[i]
                i +=1
                if int("".join(new_nums),2) % 2 ==1:
                    return "".join(new_nums)