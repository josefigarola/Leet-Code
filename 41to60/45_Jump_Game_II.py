class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1 = 0
        p2 = 0
        count = 0

        while(p2 < len(nums)-1):
            jump = 0
            for i in range(p1, p2+1):
                jump = max(jump, i+nums[i])
            p1 = p2+1
            p2 = jump
            count += 1
        return count



