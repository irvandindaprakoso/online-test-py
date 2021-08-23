/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    nums.sort();
    let current = null;
    for (let i=0; i< nums.length; i++){
        if (i == 0){
            if (nums[i] != nums[i+1]){
                return nums[i];
            }
        }        
        else{
            if (nums[i] != nums[i+1] && nums[i] != nums[i-1]){
                return nums[i];
            }
            
        }
    }
};
