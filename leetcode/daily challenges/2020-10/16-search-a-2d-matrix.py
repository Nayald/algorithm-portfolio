class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        n = len(matrix) * len(matrix[0])
        lo = 0
        hi = n
        while lo < hi:
            mid = (lo + hi) // 2
            i, j = mid // len(matrix[0]), mid % len(matrix[0])
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                lo = mid + 1
            else:
                hi = mid
                
        return False