class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(': ')', '{': '}', '[': ']'}    
        if not s:
            return True
        
        stack = []
        for i in range(len(s)):
            if s[i] in pairs.keys():
                stack.append(s[i])
            elif not stack or s[i] != pairs[stack.pop()]:
                return False
        
        return not stack