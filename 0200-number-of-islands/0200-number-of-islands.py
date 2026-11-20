from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and visited[r][c] == 0:
                    count += 1
                    self.bfs(r,c,grid,visited,rows,cols)
        return count

    def bfs(self,r,c,grid,visited,rows,cols):
        queue = deque()
        queue.append((r,c))
        visited[r][c] = 1
        while len(queue) != 0:
            i,j = queue.popleft()
            for x, y in [(-1,0),(0,-1),(1,0),(0,1)]:
                new_i, new_j = i+x, j+y
                if new_i < 0 or new_j < 0 or new_i >= rows or new_j >= cols:
                    continue
                if grid[new_i][new_j] == "0":
                    continue
                if visited[new_i][new_j] == 1:
                    continue
                visited[new_i][new_j] = 1
                queue.append((new_i, new_j)) 
