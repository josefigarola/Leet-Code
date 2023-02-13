class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p1 = 0
        output = []
        output.append(nums[p1])
        while (p1 < len(nums)-1):
            print(output)
            p1 = p1 + 1
            output.append(nums[p1] + output[p1-1])

        print(output)
    
Solution = Solution()
nums = [1,1,1,1,1]
Solution.runningSum(nums)