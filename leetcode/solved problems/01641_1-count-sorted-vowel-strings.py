class Solution:
    def countVowelStrings(self, n: int) -> int:
        v = ["a", "e", "i", "o", "u"]
        result = v
        for i in range(1, n):
            result = [x + y for x in result for y in v[v.index(x[-1]):]]
            
        return len(result)
                    
                