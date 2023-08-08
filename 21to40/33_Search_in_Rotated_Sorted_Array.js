/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let p1 = 0;
    let p2 = nums.length-1;
    let mid = p1+Math.floor((p2-p1)/2);
    while(p1!=p2){
        mid = p1+Math.floor((p2-p1)/2);
        
        if(nums[mid] == target) return mid; // mid is target
        
        if(nums[mid] >= nums[p1]){ // check on left side
            if(target>=nums[p1] && target<=nums[mid]){ // check if in range
                p2 = mid - 1; // move p2 to mid
            }
            else{
                p1 = mid + 1; // move p1 to mid
            }
        }
        else{ // find val
            if(nums[p2] >= target && nums[mid] <= target){
                p1 = mid + 1;
            }
            else{
                p2 = mid - 1;
            }
        }
    }
    if(nums[p1] == target){
        return p1;
    }
    return -1;

};
