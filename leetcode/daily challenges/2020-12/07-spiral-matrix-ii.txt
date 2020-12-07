class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        v = 1
        i = j = 0
        k = 0
        while k < n:
            for j in range(k, n):
                matrix[i][j] = v
                v += 1
                
            k += 1
            for i in range(k, n):
                matrix[i][j] = v
                v += 1
                
            n -= 1
            k -= 1
            for j in reversed(range(k, n)):
                matrix[i][j] = v
                v += 1
            
            k += 1
            for i in reversed(range(k, n)):
                matrix[i][j] = v
                v += 1
            
        return matrix