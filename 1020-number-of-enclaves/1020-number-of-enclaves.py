class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0 or r == rows-1 or c == cols-1:
                    if grid[r][c] == 1 and visited[r][c] == 0:
                        self.dfs(r,c,visited,grid,rows,cols)
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and visited[r][c] == 0:
                    count += 1
        return count

    def dfs(self,r,c,visited,grid,rows,cols):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return
        if grid[r][c] == 0:
            return
        if grid[r][c] == 1 and visited[r][c] == 1:
            return
        visited[r][c] = 1
        self.dfs(r-1,c,visited,grid,rows,cols)
        self.dfs(r,c-1,visited,grid,rows,cols)
        self.dfs(r+1,c,visited,grid,rows,cols)
        self.dfs(r,c+1,visited,grid,rows,cols)
