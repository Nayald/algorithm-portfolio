from functools import lru_cache

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:               
        @lru_cache
        def helper(i, j):
            if i >= len(matrix) or j >= len(matrix[0]):
                return False
            
            if matrix[i][j] == target:
                return True
            
            return helper(i + 1, j) or helper(i, j + 1)
        
        return helper(0, 0)