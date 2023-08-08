class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        if(n == 0):
            return -1
        
        p1, p2 = 0, n - 1
        
        while(p1 <= p2):
            # Get the middle
            mid = p1 + (p2 - p1) // 2
            
            # Check if target is at mid
            if(nums[mid] == target):  
                return mid
            
            # p1 half is sorted
            if(nums[p1] <= nums[mid]):  
                # Target is in the p1 half
                if(nums[p1] <= target <= nums[mid]): 
                    p2 = mid - 1
                else:
                    p1 = mid + 1
            else: 
                # Target is in the p2 half
                if(nums[mid] <= target <= nums[p2]): 
                    p1 = mid + 1
                else:
                    p2 = mid - 1
        
        return -1