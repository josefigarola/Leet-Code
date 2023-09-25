class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(set(x for x in nums if x > 0))
        n = len(nums)
        print(nums)

        for i in range(n):
            if(nums[i] != i + 1):
                return i + 1

        return n+1
        