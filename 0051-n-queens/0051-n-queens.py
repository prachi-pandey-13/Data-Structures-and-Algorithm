class Solution:
    def solve(self, col, result, board, leftrow, lowerdiag, upperdiag, n):
        if col == n:
                result.append(board[:])
                return
        for row in range(0, n):
            if leftrow[row] == 0 and lowerdiag[row+col] == 0 and upperdiag[n-1+col-row] == 0:
                board[row] = board[row][:col] + "Q" + board[row][col+1:]

                leftrow[row] = 1
                lowerdiag[row+col] = 1
                upperdiag[n-1 + col-row] = 1
                self.solve(col+1, result, board, leftrow, lowerdiag, upperdiag, n)  
                
                board[row] = board[row][:col] + "." + board[row][col+1:]
                leftrow[row] = 0
                lowerdiag[row+col] = 0
                upperdiag[n-1 + col-row] = 0

    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = ["." * n for _ in range(n)]
        leftrow = [0]*n
        lowerdiag = [0] * (2*n-1)
        upperdiag = [0] * (2*n-1)
        self.solve(0, result, board, leftrow, lowerdiag, upperdiag,n)
        return result