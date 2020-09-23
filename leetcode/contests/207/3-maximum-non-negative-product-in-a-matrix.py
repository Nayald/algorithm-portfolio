class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        dp = [[[0, 0] for i in range(len(grid[0]))] for j in range(len(grid))]
        dp[0][0] = [grid[0][0], grid[0][0]]
        
        def f(i, j):
            if i >= len(grid) or j >= len(grid[0]):
                return 
            
            old = dp[i][j][:]
            dp[i][j][0] = min(*([dp[i-1][j][0] * grid[i][j], dp[i-1][j][1] * grid[i][j]] if i > 0 else []), *([dp[i][j-1][0] * grid[i][j], dp[i][j-1][1] * grid[i][j]] if j > 0 else []))
            dp[i][j][1] = max(*([dp[i-1][j][0] * grid[i][j], dp[i-1][j][1] * grid[i][j]] if i > 0 else []), *([dp[i][j-1][0] * grid[i][j], dp[i][j-1][1] * grid[i][j]] if j > 0 else []))
        
            if dp[i][j] != old:
                f(i+1,j)
                f(i,j+1)
            
        
        f(1,0)
        f(0,1)
        return (dp[-1][-1][1] % 1000000007) if dp[-1][-1][1] >= 0 else -1
        