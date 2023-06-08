class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        out = 0

        # [[7,-3]] or [[-1]]
        if(len(grid) == 1):
            for i in range(len(grid[0])):
                if(grid[0][i] < 0):
                    out += 1
            return out


        for i in range(0,len(grid)):
            for j in range(0,len(grid[1])):
                print(i,j)
                #print(grid[i][j])
                if(grid[i][j] < 0):
                    out += 1

        print(out)
        return out