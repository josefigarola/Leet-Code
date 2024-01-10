class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # if matrix doesnt exists
        if(not matrix or not matrix[0]):
            return []

        m, n = len(matrix), len(matrix[0])
        output = [0] * (m * n)

        RS = 0  # Row start
        RE = m - 1  # Row end
        CS = 0  # Column start
        CE = n - 1  # Column end

        index = 0  # index for output

        while(RS <= RE and CS <= CE):
            # from left to right
            for i in range(CS, CE + 1):
                output[index] = matrix[RS][i]
                index += 1
            RS += 1

            # from up to down
            for i in range(RS, RE + 1):
                output[index] = matrix[i][CE]
                index += 1
            CE -= 1

            # check if the are more rows
            if(RS <= RE):
                # from right to left
                for i in range(CE, CS - 1, -1):
                    output[index] = matrix[RE][i]
                    index += 1
                RE -= 1

            # check if the are more columns
            if(CS <= CE):
                # from bottom to up
                for i in range(RE, RS - 1, -1):
                    output[index] = matrix[i][CS]
                    index += 1
                CS += 1

        return output