class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        from copy import deepcopy
from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        gridcopy = deepcopy(grid)
        rows = len(gridcopy)
        cols = len(gridcopy[0])
        fresh_count = 0
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if gridcopy[r][c] == 2:
                    queue.append((r,c))
                elif gridcopy[r][c] == 1:
                    fresh_count += 1

        minutes = 0
        while len(queue) != 0 and fresh_count > 0:
            minutes += 1
            total_rotten  = len(queue)
            for _ in range(total_rotten):
                i,j = queue.popleft()
                for x, y in [(-1,0),(0,1),(1,0),(0,-1)]:
                    new_i = i+x
                    new_j = j+y
                    if new_i < 0 or new_i == rows or new_j < 0 or new_j == cols:
                        continue
                    if gridcopy[new_i][new_j] == 0 or gridcopy[new_i][new_j] == 2:
                        continue
                    fresh_count -= 1
                    gridcopy[new_i][new_j] = 2
                    queue.append((new_i, new_j))
        if fresh_count > 0:
            return -1
        return minutes
                
                    

