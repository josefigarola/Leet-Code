class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[0]

        # Phase 1: Find the intersection point in the cycle
        while(True):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if(slow == fast):
                break

        # Phase 2: Find the entrance to the cycle
        slow = nums[0]
        while(slow != fast):
            slow = nums[slow]
            fast = nums[fast]

        return slow
        