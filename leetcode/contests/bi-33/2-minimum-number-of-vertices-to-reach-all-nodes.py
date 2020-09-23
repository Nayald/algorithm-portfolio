class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        arr = [0] * n
        for s, e in edges:
            arr[e] += 1
            
        result = []
        for i, e in enumerate(arr):
            if e == 0:
                result.append(i)
                
        return result
            