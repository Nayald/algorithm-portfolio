class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        count = [0] * 7
        counta = [0] * 7
        countb = [0] * 7
        for a, b in zip(A, B):
            count[a] += 1
            counta[a] += 1
            if b != a:
                count[b] += 1
            
            countb[b] += 1
        
        result = float("inf")
        for i, v in enumerate(count):
            if v < n:
                continue
                
            result = min(result, n - max(counta[i], countb[i]))
                
        return result if result != float("inf") else -1