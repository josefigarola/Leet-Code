class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(height) - 1

        if(len(height) == 1):
            return height[0]

        while(left < right):
            # difference between indices
            width = right - left
            
            #  (minimum of the two heights)
            container_height = min(height[left], height[right])
            
            # Calculate the area of the container and update max_water if needed
            area = width * container_height
            maxArea = max(maxArea, area)
            
            # Move the pointers towards each other based on which side has the shorter height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea