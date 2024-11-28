"""Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # loop through all squares, if the square is a piece of land then perform dfs and mark it as zero 
        # after encountering a 1, dfs should flip all connected land to 0

        num_islands = 0

        def dfs(i, j):
            grid[i][j] = '0'
            for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= i+a < len(grid) and 0 <= j+b < len(grid[0]) and grid[i+a][j+b] == '1':
                    dfs(i+a, j+b)

        for i, row in enumerate(grid): 
            for j, square in enumerate(row): 
                if square   == '1':
                    num_islands += 1
                    dfs(i, j)
                    
        return num_islands                    