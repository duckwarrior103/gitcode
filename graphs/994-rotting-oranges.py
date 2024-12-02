'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
'''

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rotten_oranges = 0
        total_oranges = 0

        # find all the rotten oranges 
        q = deque()

        for i, row in enumerate(grid):
            for j, orange in enumerate(row):
                if orange == '1':
                    total_oranges += 1
                elif orange == '2':
                    q.append((i, j))
                    total_oranges += 1
                

        minutes = 0

        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                grid[i, j] = '2'
                rotten_oranges += 1
                # check neighbors of orange that just rot and add to queue, mark them as '3' for in queue
                for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= i+a < len(grid) and 0 <= j+b < len(grid[0]) and grid[i+a][j+b] == '1':
                        grid[i+a][j+b] = '3'
                        q.append((i+a, j+b))
                
            if q:
                minutes += 1
        
        return minutes if rotten_oranges == total_oranges else -1

