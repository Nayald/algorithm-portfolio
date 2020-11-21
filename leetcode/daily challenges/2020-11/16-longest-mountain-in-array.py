class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        
        hi = 0
        i = 0
        while i < len(A):
            last = A[i]
            j = i + 1
            while j < len(A) and A[j] > last:
                last = A[j]
                j += 1
                
            if j > i + 1:
                k = j
                while k < len(A) and A[k] < last:
                    last = A[k]
                    k += 1
                
                if k > j:
                    hi = max(hi, k - i)
                    
                j = k - 1
                    
            i = j
        
        return hi