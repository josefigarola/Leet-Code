class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        '''
        for i in range(len(nums)):
            for j in range(0, i):
                if (nums[i] == nums[j]):
                    return True
        return False
        '''
    
        '''
        nums.sort()
        for i in range(len(nums)):
            for j in range(0, i):
                if (nums[i] == nums[j]):
                    return True
        return False
        '''
        
        data = set()
        for i in nums:
            if i in data:
                return True
            data.add(i)
        return False
