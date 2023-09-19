class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def hasDuplicates(nums):
            seen = set()
            for num in nums:
                if num != ".":
                    if num in seen:
                        return True
                    seen.add(num)
            return False

        # Check rows
        for row in board:
            if hasDuplicates(row):
                return False

        # Check columns
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if hasDuplicates(column):
                return False

        # Check 3x3 subgrids (boxes)
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid = []
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        subgrid.append(board[x][y])
                if hasDuplicates(subgrid):
                    return False

        return True