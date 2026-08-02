class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        rowtrack = [0] * rows
        coltrack = [0] * cols
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rowtrack[i] = -1
                    coltrack[j] = -1

        for i in range(rows):
            for j in range(cols):
                if rowtrack[i] == -1 or coltrack[j] == -1:
                    matrix[i][j] = 0