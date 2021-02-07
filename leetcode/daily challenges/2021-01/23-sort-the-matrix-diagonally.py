import heapq

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        heap = []
        for k in range(len(mat)):
            i = k
            j = 0
            while i < len(mat) and j < len(mat[0]):
                heapq.heappush(heap, mat[i][j])
                i += 1
                j += 1
                
            i = k
            j = 0
            while heap:
                mat[i][j] = heapq.heappop(heap)
                i += 1
                j += 1
                
        for k in range(1, len(mat[0])):
            i = 0
            j = k
            while i < len(mat) and j < len(mat[0]):
                heapq.heappush(heap, mat[i][j])
                i += 1
                j += 1
                
            i = 0
            j = k
            while heap:
                mat[i][j] = heapq.heappop(heap)
                i += 1
                j += 1
                
        return mat