class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        # UPPER ROW
        r, c = 0, 0
        for c in range(cols):
            if board[r][c] == "O" and visited[r][c] == 0:
                self.dfs(r, c, rows, cols, board, visited)

        # LAST ROW
        r, c = rows-1, 0
        for c in range(cols):
            if board[r][c] == "O" and visited[r][c] == 0:
                self.dfs(r, c, rows, cols, board, visited)
        # FIRST COLUMN
        r, c = 0,0
        for r in range(rows):
            if board[r][c] == "O" and visited[r][c] == 0:
                self.dfs(r,c, rows, cols, board, visited)
        # LAST COLUMN
        r, c = 0, cols-1
        for r in range(rows):
            if board[r][c] == "O" and visited[r][c] == 0:
                self.dfs(r,c, rows, cols, board, visited)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and visited[r][c] == 0:
                    board[r][c] = "X"


    def dfs(self, r, c, rows, cols, board, visited):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if visited[r][c] == 1:
            return
        if board[r][c] == "X":
            return
        visited[r][c] = 1
        self.dfs(r-1, c, rows, cols, board, visited)
        self.dfs(r, c-1, rows, cols, board, visited)
        self.dfs(r+1, c, rows, cols, board, visited)
        self.dfs(r, c+1, rows, cols, board, visited)        
