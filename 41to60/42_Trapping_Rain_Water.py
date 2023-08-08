class Solution(object):
    def GetUnits(self,p1,p2,height,units,elevations):
        # get the len of the area
        diff = abs(p2-p1) - 1 
        # get the optimal elevation point
        if(height[p1]>p2):
            h = height[p2]
        else:
            h = height[p1]
        # Compute total area and substract the other elevation points
        totalArea = (diff*h)
        # get the total value of elevations inside area
        elevationHeight = height[p1+1:p2]
        for i in range(len(elevationHeight)):
            elevations += elevationHeight[i]
        # get the units of water
        print('Water b',[units,totalArea,elevations])
        units += (totalArea - elevations)
        print('Water a',[units,totalArea,elevations])
        # move pointers to next elevations
        p1 = p2
        p2 += 1

        return p1,p2,units

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p1 = 0
        n = len(height)
        units = 0

        # If there is only one elevation
        if(n == 1 or n==2):
            return 0
        
        # start where there is an elevation
        while(height[p1] == 0):
            p1 += 1
        # p2 after p1
        p2 = p1+1

        while(p1 < n-1):
            elevations = 0
            print('pointers', p1,p2)
            # if the height of p2 lower than p1
            if(height[p1] > 0 and height[p2] < height[p1]):
               p2 += 1
            # if the height of p2 is equal or greater than p1 and p1 greater than 0
            if(p2<=n-1):
                if(height[p1] > 0 and height[p2] >= height[p1] and p2 <= n-1):
                    p1,p2,units = self.GetUnits(p1,p2,height,units,elevations)
            else:
                return abs(units)
            # if pointer 2 reaches the end
            if(p2 == n-1):
                # if height is lower than p1 then theres no water
                if(height[p2-1] < height[p2]):
                    p1,p2,units = self.GetUnits(p1,p2,height,units,elevations)
                # There might be water trapped
                else:
                    p2 = p1 + 1
                    height[p1] = height[p1] - 1
                if(height[p1] < 0):
                    return abs(units)
        
            print('Units ',units)
        return abs(units)