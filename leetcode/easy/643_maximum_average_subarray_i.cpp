/*
 * 643. Maximum Average Subarray I
 * Platform: LEETCODE
 * Difficulty: easy
 * Language: cpp
 * Problem URL: https://leetcode.com/problems/maximum-average-subarray-i/
 * Date: 2025-06-13T16:57:52.126Z
 * Author: CodeSync Extension
 */

class·‌Solution·‌{public:·‌·‌·‌·‌double·‌findMaxAverage(vector<int>&·‌nums,·‌int·‌k)·‌{·‌·‌·‌·‌·‌·‌·‌·‌double·‌average;·‌·‌·‌·‌·‌·‌·‌·‌double·‌k_sum·‌=·‌0;·‌·‌·‌·‌·‌·‌·‌·‌for·‌(int·‌i=0;·‌i·‌<k;·‌i++){·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌k_sum·‌+=nums[i];        }        average = float(k_sum)/k;        for(int i = k; i < nums.size(); i++){