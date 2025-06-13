/*
 * 2616. Minimize the Maximum Difference of Pairs
 * Platform: LEETCODE
 * Difficulty: medium
 * Language: cpp
 * Problem URL: https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/editorial/
 * Date: 2025-06-13T06:24:54.484Z
 * Author: CodeSync Extension
 */

·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌while·‌i·‌+·‌1·‌<·‌N:·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌i·‌=·‌0·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌if·‌nums[i+1]-nums[i]·‌<=target:·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌pairs·‌+=1·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌i·‌+=2·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌else:·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌i·‌+=1·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌return·‌pairs·‌>=p·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌pairs·‌=0·‌·‌·‌·‌·‌·‌·‌·‌l,·‌r·‌=·‌0,·‌nums[-1]·‌-·‌nums[0]·‌·‌·‌·‌·‌·‌·‌·‌best·‌=·‌r·‌·‌·‌·‌·‌·‌·‌·‌while·‌l·‌<=·‌r:·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌mid·‌=·‌(l+r)//2·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌if·‌possible_pair(mid):·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌best·‌=·‌mid·‌·‌·‌·‌·‌·‌·‌·‌·‌N·‌=·‌len(nums)·‌·‌·‌·‌·‌·‌·‌·‌def·‌possible_pair(target):    def minimizeMax(self, nums: List[int], p: int) -> int:·‌·‌·‌·‌·‌·‌·‌·‌nums.sort()class Solution: