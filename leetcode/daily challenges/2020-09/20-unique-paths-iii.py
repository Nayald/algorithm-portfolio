class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        
        nb_path = 0
        def find_paths(i, j, remain):
            nonlocal nb_path
            
            if grid[i][j] == -1:
                return
            
            if grid[i][j] == 2 and remain == 1:
                nb_path += 1
                return 
            
            old = grid[i][j]
            grid[i][j] = -1    
            if 0 <= (i - 1) < r:
                find_paths(i - 1, j, remain - 1)
                
            if 0 <= (i + 1) < r:
                find_paths(i + 1, j, remain - 1)
                
            if 0 <= (j - 1) < c:
                find_paths(i, j - 1, remain - 1)
                
            if 0 <= (j + 1) < c:
                find_paths(i, j + 1, remain - 1)
            
            grid[i][j] = old
        
        
        nb_cells = r * c
        start = (0, 0)
        for i in range(r):
            for j in range(c):
                if grid[i][j] == -1:
                    nb_cells -= 1
                elif grid[i][j] == 1:
                    start = (i, j)
                    
        find_paths(*start, nb_cells)
        return nb_path