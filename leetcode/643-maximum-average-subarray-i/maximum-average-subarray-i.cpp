class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double average;
        double k_sum = 0;
        for (int i=0; i <k; i++){
            k_sum +=nums[i];
        }

        average = double(k_sum)/k;
        for(int i = k; i < nums.size(); i++){
            k_sum +=nums[i]  - nums[i-k];
            average = max(average, double(k_sum)/k);
        }

        return average;

        
    }
};