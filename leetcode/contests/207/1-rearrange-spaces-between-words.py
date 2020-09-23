class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = 0
        for c in text:
            if c == " ":
                spaces += 1
                
        words = text.split()
        try:
            inspace = spaces // (len(words) - 1)
        except:
            inspace = 0
            
        outspace = spaces - inspace * (len(words) - 1)
        
        return (" "*inspace).join(words) + " " * outspace