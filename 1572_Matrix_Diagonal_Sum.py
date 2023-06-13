class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        first = 0
        second = 0
        out = 0

        # testcase
        if(n == 1):
            return mat[0][0]

        # get the primary diagonal
        for i in range(0,n):
            #print(i,mat[i][i])
            first += mat[i][i]

        # get the secondary diagonal
        for i in range(0,n):
            #print(-i+n-1,mat[-i+n-1][i])
            second += mat[-i+n-1][i]

        # check if the matrix is even or odd
        if(n % 2 != 0):
            #tmp = n//2
            #print(tmp)
            center = mat[n//2][n//2]
            #print(center)
            out -= center
            #print(out)

        out += first + second
        return out