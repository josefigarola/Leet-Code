class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if(not matrix):
            return

        rows, cols = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        #  Mark rows and columns to be zeroed
        for i in range(rows):
            for j in range(cols):
                if(matrix[i][j] == 0):
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Set rows and columns to zero
        for i in range(rows):
            for j in range(cols):
                if(i in zero_rows or j in zero_cols):
                    matrix[i][j] = 0
        