class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        d = {}
        for v in nums:
            if v not in d:
                d[v] = 1
            else:
                d[v] += 1
                
        result = 0
        for v in d.values():
            if v == 1:
                continue
                
            if v == 2:
                result += 1
            else:
                result += int(factorielle(v) / (factorielle(2) * factorielle(v - 2)))
            
        return result
            

def factorielle(n):
    if n <= 2:
        return n
    
    result = 2
    while n > 2:
        result *= n
        n -= 1
        
    return result