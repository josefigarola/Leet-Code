class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0;
        int right = nums.size()-1;
        int mid = left+(right-left)/2;
        // check if it is rotated
        if(nums[left]<nums[right]){ // first numer is smaller than last
            return nums[left];
        }
        if(nums.size()==1){
            return nums[0];
        }
        // is rotated
        left = 1;
        // binary search
        while(left <= right){
            mid = left+(right-left)/2;
            if(nums[mid-1]>nums[mid]){
                return nums[mid];
            }
            cout << nums[mid] << endl;
            // check if mid is greater than last element
            if(nums[mid] > nums[right]){
                left = mid+1;
                    
            }
            else{
                right = mid - 1;
            }
        }   
        return nums[left];
    }
};
