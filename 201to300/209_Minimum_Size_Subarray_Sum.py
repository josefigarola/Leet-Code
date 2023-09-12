class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        min_len = float('inf')

        # sliding window approach
        for right in range(len(nums)):
            total += nums[right]

            while(total >= target):
                #print(left,right)
                min_len = min(min_len, right-left+1)
                total -= nums[left]
                left+=1

        if(min_len > len(nums)):
            return 0
        return min_len
