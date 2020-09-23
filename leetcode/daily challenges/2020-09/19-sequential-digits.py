class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        
        def append(val, i):
            if i > 9:
                return 
            
            val = val * 10 + i
            if low <= val <= high:
                result.append(val)
                
            if val < high:
                append(val, i+1)
                
        for i in range(1, 9):
            append(0, i)
            
        return sorted(result)