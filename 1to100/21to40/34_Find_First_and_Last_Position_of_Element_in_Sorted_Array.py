class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = -1
        second = -1

        # Test case, empty array
        if(len(nums) == 0):
            return [first,second]

        # Find the first value
        p1 = 0
        p2 = len(nums)-1
        first = -1
        mid = p1 + (p2 - p1) // 2

        while(p1 <= p2):
            mid = p1 + (p2 - p1) // 2
            if(nums[mid] >= target):
                p2 = mid - 1
            else:
                p1 = mid + 1
            
            if(nums[mid] == target):
                first = mid

        if(first == -1):
            return [-1, -1]
                
        # Find the second value
        p1 = 0
        p2 = len(nums)-1
        second = -1
        while(p1 <= p2):
            mid = p1 + (p2 - p1) // 2
            if(nums[mid] <= target):
                p1 = mid + 1
            else:
                p2 = mid - 1
            
            if(nums[mid] == target):
                second = mid

        return [first,second]

