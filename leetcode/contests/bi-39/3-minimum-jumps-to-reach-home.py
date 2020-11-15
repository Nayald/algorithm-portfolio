from collections import Counter
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        axis = [float("inf")] * 5000
        for f in forbidden:
            axis[f] = -1
        
        axis[0] = 1
        axis[x] = -1
        def helper(pos=0, n=0, back=True):
            if pos == x:
                axis[pos] = n
                return True
            
            if axis[pos] == -1:
                return False
            
            if n >= axis[pos]:
                return False
            
            axis[pos] = n
            if back and pos - b > 0:
                helper(pos - b, n + 1, False)
            
            if pos < 5000 - a:
                if helper(pos + a, n + 1, True):
                    return True
            
              
        helper()
        return axis[x]
    
            