class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        list1 = []
        list2 = []
        n1 = len(nums1)
        n2 = len(nums2)

        for i in range(n1):
            if(nums1[i] not in nums2 and nums1[i] not in list1):
                    list1.append(nums1[i])
        
        for i in range(n2):
            if(nums2[i] not in nums1 and nums2[i] not in list2):
                list2.append(nums2[i])

        #print([list1,list2])
        return [list1,list2]        