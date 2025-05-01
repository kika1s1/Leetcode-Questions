/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let ans = []
    for(let index = 0; index < arr.length; index += size){
        ans.push(arr.slice(index, index+size))
    }
    return ans
    
};
