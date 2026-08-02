class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n-1):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        

        # n = len(matrix)
        # result = [[0 for _ in range(n)] for _ in range(n)]
        # for i in range(n):
        #     for j in range(n):
        #         matrix[i][j] = result[j][n-i-1]
        # return result