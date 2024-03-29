class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # check if len is 1
        if(numRows == 1 or numRows >= len(s)):
            return s

        result = [''] * numRows
        row, step = 0, 1
        
        for char in s:
            result[row] += char
            
            if(row == 0):
                step = 1
            elif(row == numRows - 1):
                step = -1
            
            row += step
        
        return ''.join(result)
