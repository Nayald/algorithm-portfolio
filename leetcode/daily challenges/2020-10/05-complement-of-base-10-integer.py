class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        
        result = 0
        i = 1
        while i <= N:
            if N & i == 0:
                result += i
            
            i <<= 1
                
        return result
