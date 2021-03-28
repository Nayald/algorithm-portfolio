class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        r = 0
        i = 0
        while i < len(s):
            c = mapping[s[i]]
            c2 = 0
            if i + 1 < len(s):
                c2 = mapping[s[i+1]]
            if c < c2:
                r += c2 - c
                i += 2
            else:
                r += c
                i += 1
        
        return r