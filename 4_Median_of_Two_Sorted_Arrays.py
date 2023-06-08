class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #n = len(nums1)
        #m = len(nums2)
        tmp = nums1 + nums2
        tmp.sort()
        nums3 = tmp

        # Even array
        if(len(nums3) % 2 == 0):
            # print('even')
            p1 = len(nums3)//2 - 1 
            p2 = len(nums3) - len(nums3)//2
            return (nums3[p1] + nums3[p2])*0.5
        else:
            # Odd array
            # print('odd')
            return nums3[len(nums3)/2]