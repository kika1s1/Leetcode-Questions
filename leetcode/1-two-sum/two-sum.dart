class Solution {
  List<int> twoSum(List<int> nums, int target) {
    final Map<int, int> vals = {};
    for (int i = 0; i < nums.length; i++) {
      final int val = nums[i];
      if (vals.containsKey(target - val)) {
        return [i, vals[target - val]!];
      } else {
        vals[val] = i;
      }
    }
    return [];
  }
}