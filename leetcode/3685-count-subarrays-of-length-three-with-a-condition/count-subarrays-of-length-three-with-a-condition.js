/**
 * @param {number[]} nums
 * @return {number}
 */
var countSubarrays = function(nums) {
    let count = 0
    for (let index = 2; index < nums.length; index ++ ){
        let two_sum = nums[index-2] + nums[index]
        if (two_sum ===(nums[index-1]/2) ){
            count +=1
        }
    }
    return count 
};