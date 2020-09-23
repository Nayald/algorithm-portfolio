class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def seek(val, prev, current):            
            for pos in ((current[0] + 1, current[1]), (current[0] - 1, current[1]), (current[0], current[1] + 1), (current[0], current[1] - 1)):
                if 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]) and pos != prev and grid[pos[0]][pos[1]] in {val, val.upper()}:
                    if grid[pos[0]][pos[1]] == val.upper():
                        return True
                    
                    grid[pos[0]][pos[1]] = grid[pos[0]][pos[1]].upper()
                    if seek(val, current, pos):
                        return True
            
            return False
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if ord("a") <= ord(grid[i][j]) <= ord("z"):
                    if seek(grid[i][j], (-1, -1), (i,j)):
                        return True
                
        return False
        
            