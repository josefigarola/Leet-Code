class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        maxArea = 0

        if(len(height) == 1):
            return height[0]

        for i in range(0,len(height)):
            p1,p2 = i,i+1
            while(p1<=len(height) and p2<len(height)):
                #print(height[p1],height[p2])
                h = 0
                if(height[p2] < height[p1]):
                    h = height[p2]
                else:
                    h = height[p1]

                if((p2-p1)*h > maxArea):
                    maxArea = (p2-p1)*h
                #print('Area ',maxArea)
                p2+=1
        return maxArea
