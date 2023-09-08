class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if(not height):
            return 0

        total_water = 0
        max_index = 0
        max_height = float('-inf')

        # Find the index of the maximum height
        for i in range(len(height)):
            if(height[i] > max_height):
                max_height = height[i]
                max_index = i

        # Calculate water trapped on the left side of the maximum height
        left_max = height[0]
        for i in range(1, max_index):
            if(left_max < height[i]):
                left_max = height[i]
            total_water += left_max - height[i]

        # Calculate water trapped on the right side of the maximum height
        right_max = height[-1]
        for i in range(len(height) - 2, max_index, -1):
            if(right_max < height[i]):
                right_max = height[i]
            total_water += right_max - height[i]

        return total_water