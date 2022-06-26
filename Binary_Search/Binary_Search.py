class Solution(object):
    def search(self, nums, target):
        
        p1 = 0 # left pointer
        p2 = len(nums)-1 # right pointer
        
        # while length is good
        while(p1 <= p2):
            # Get middle
            middle = p1 + (p2-p1)/2
            # Cases
            # target is in middle
            if(nums[middle] == target):
                return middle
            # target is in minor bound
            if(target < nums[middle]):
                p2 = middle - 1 
            # target is in upper bound
            if(target > nums[middle]):
                p1 = middle + 1
        
        return -1