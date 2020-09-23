from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        if not secret:
            return "0A0B"
        
        s = [c for c in secret]
        g = [c for c in guess]
        
        d = defaultdict(int)
        a = 0
        for i in range(len(s)):
            if guess[i] == secret[i]:
                a += 1
                s[i] = ""
                g[i] = ""
            else:
                d[s[i]] += 1
             
        b = 0
        for c in g:
            if c == "":
                continue
            if c in d and d[c] > 0:
                b += 1
                d[c] -= 1
                
        return str(a) + "A" + str(b) + "B"