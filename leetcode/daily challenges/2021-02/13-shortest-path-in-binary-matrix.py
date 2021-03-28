import heapq

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def orthogonalDist(a, b):
            dx = abs(a[0] - b[0])
            dy = abs(a[1] - b[1])
            return max(dx, dy)
        
        n = len(grid) - 1
        m = len(grid[0]) - 1
        
        queue = []
        heapq.heapify(queue)
        heapq.heappush(queue, (0, 1, 0, 0)) # dist, v, i, j
        while queue:
            _, v, i, j = heapq.heappop(queue)
            if not (0 <= i <= n and 0 <= j <= m and grid[i][j] == 0):
                continue
            
            grid[i][j] = 8
            #print(i, j)
            if i == n and j == m:
                print(*[row for row in grid], sep="\n")
                return v
            
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    heapq.heappush(queue, (v + orthogonalDist((i + dx, j + dy), (n, m)), v + 1, i + dx, j + dy))
            
        return -1