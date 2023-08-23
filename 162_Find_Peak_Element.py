class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peak = 0
        n = len(nums)
        p1 = 0
        p2 = n-1

        #print(nums)

        if(n == 1):
            return peak

        while(p1 <= p2):
            #print('p1',[p1,nums[p1]], 'p2',[p2,nums[p2]])
            if(nums[p1] > nums[peak]):
                peak = p1
                #print('peak',peak)
            if(nums[p2] > nums[peak]):
                peak = p2
                #print('peak',peak)
            
            p1 += 1
            p2 -= 1

        return peak