# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

t = int(input())
 
for i in range(t):
  a = int(input())
 
  nums = [int(i) for i in input().split()]
  ans = 0
 
  def divide(left, right, nums):
    global ans
    if left == right:
      return [nums[left]],True
    
    mid = left + (right - left) // 2
 
    left_sub, can_left = divide(left, mid, nums)
    right_sub, can_right = divide(mid + 1, right, nums)
 
    if not (can_left and can_right):
      return left_sub + right_sub, False
 
    left_min, left_max = min(left_sub), max(left_sub)
    right_min, right_max = min(right_sub), max(right_sub)
 
    if left_min < right_min and left_max < right_min:
        return left_sub + right_sub, True
    

    elif left_min > right_min and left_min > right_max:
      left_sub, right_sub = right_sub, left_sub
      ans += 1
      return left_sub + right_sub , True   
    
    return left_sub + right_sub , False
  x, y = (divide(0, a-1,  nums))
 
  if y:
    print(ans)
  else:
    print(-1) 