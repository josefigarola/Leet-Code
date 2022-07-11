class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int left = 0;
        int right = nums.size()-1;
        int n = right; // indexing 
        vector<int>squaredvec(nums.size());
        
        /*
        if(nums.size() == 1){
            nums[0] = nums[0]*nums[0];
            return nums;
        }*/
        
        while(left<=right){
            int pow1 = nums[left]*nums[left]; // square from beginning
            int pow2 = nums[right]*nums[right]; // square of ending
            
            // check which pow is bigger (within negs and pos nums)
            if(pow1 > pow2){ // if left square is bigger
                squaredvec[n--] = pow1; // nth musy be starting element
                left++; // increment left 
            }
            else{
                squaredvec[n--] = pow2;
                right--;
            }
        }
        return squaredvec;
    }
};
