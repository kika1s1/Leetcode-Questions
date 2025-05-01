class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        length = len(nums)

        def get_next_index(current_index):
            return (current_index + nums[current_index]) % length

        for i in range(length):
            if nums[i] == 0:
                continue
          
            slow_pointer = i
            fast_pointer = get_next_index(i)
          
            while nums[slow_pointer] * nums[fast_pointer] > 0 and nums[slow_pointer] * nums[get_next_index(fast_pointer)] > 0:
                if slow_pointer == fast_pointer:
                    if slow_pointer != get_next_index(slow_pointer):
                        return True
                    break
              
                slow_pointer = get_next_index(slow_pointer)
                fast_pointer = get_next_index(get_next_index(fast_pointer))
          
            index = i
            while nums[index] * nums[get_next_index(index)] > 0:
                next_index = get_next_index(index)
                nums[index] = 0
                index = next_index

        return False