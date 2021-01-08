class Solution:
    def countArrangement(self, n: int) -> int:
        def helper(i, remainings):
            if not remainings:
                return 1
            
            return sum(helper(i+1, remainings - {v}) for v in remainings if v % i == 0 or i % v == 0)
        
        return helper(1, set(range(1, n+1)))
                    
                