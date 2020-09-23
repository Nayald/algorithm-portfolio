class Solution:
    def numSub(self, s: str) -> int:
        previous = -1
        r = [0] * len(s)
        for i in range(len(s)):
            if previous == -1 and s[i] == "1":
                previous = i
            
            if previous != -1 and s[i] == "0":
                r[i - previous - 1] += 1
                previous = -1
        
        if previous != -1:
            r[len(s) - previous - 1] += 1
                
        for i in range(len(r)):
            if r[i] > 0:
                for j in range(i):
                    r[j] += r[i] * (i - j + 1)
                   
        return sum(r) % 1000000007