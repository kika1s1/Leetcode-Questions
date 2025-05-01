/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    let goodPairCount = 0;
    /*
        iterate from 0 until nums.length
        take the current index add 1 to it and use it to initalise another lopp that iterates until nums.length
        if the outter loop nums[i] and the innerLoop nums[j] are equal
        increase good pair count

    */
    for (let i = 0; i < nums.length; i++){
        for (let j = i + 1; j < nums.length; j++)
            if (nums[i] === nums[j])
                goodPairCount += 1;
    }
    return goodPairCount;
};