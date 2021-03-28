class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        result = 0
        nested = 0
        last = None
        for c in S:
            if c == "(":
                nested += 1
            elif last == "(":
                result += 1 << (nested - 1)              
            else:
                nested -= 1
                
            last = c
            
        return result