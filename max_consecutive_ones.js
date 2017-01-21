/**
 * Given a binary array, find the maximum number of consecutive 1s in this array.
 * https://leetcode.com/problems/max-consecutive-ones/
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    var max = 0;
    var count = 0;
    for (i in nums) {
        if (nums[i] === 1) {
            count++;
            if (max < count) {
                max = count;
            }
        }
        else {
            count = 0;
        }
    }
    return max;
};
