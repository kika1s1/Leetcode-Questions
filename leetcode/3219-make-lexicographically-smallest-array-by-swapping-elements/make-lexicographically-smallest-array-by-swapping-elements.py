class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        nums_sorted = sorted(nums)

        curr_group = 0
        num_to_group = {}
        group_to_list = {curr_group: deque([nums_sorted[0]])}
        num_to_group[nums_sorted[0]] = curr_group

        for i in range(1, len(nums)):
            if abs(nums_sorted[i] - nums_sorted[i - 1]) > limit:
                curr_group += 1 
            num_to_group[nums_sorted[i]] = curr_group

            if curr_group not in group_to_list:
                group_to_list[curr_group] = deque()
            group_to_list[curr_group].append(nums_sorted[i])

        for i in range(len(nums)):
            group = num_to_group[nums[i]]  
            nums[i] = group_to_list[group].popleft()  

        return nums
