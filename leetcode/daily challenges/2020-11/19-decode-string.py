class Solution:
    def decodeString(self, s: str) -> str:
        def helper(s):
            if not s:
                return ""
            
            # check if string begin with a number
            i = 0
            while "0" <= s[i] <= "9":
                i += 1

            # if no number it is an implicit 1 and because of that we can say a number
            # is always followed by a bracket or a char
            k = int(s[:i]) if i > 0 else 1
            # for the result we can always split the problem so we can call again the 
            # function each time we finish a sub task (a number + substring | chars) 
            # with the remaining chars
            if s[i] == "[":
                # if it is followed by a bracket we need to check where it is its counterpart
                # so we have to keep track of the number of open brackets
                j = i + 1
                p = 1
                while p != 0:
                    if s[j] == "[":
                        p += 1
                    elif s[j] == "]":
                        p -=1
                    
                    j += 1
                
                return k * helper(s[i+1:j-1]) + helper(s[j:])
            else:
                j = i
                while j < len(s) and "a" <= s[j] <= "z":
                    j += 1
                    
                return k * s[i:j] + helper(s[j:])
                
                
        return helper(s)