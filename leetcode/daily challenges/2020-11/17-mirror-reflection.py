class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:        
        h, r = q, 1
        while h % p != 0:
            h += q
            r ^= 1
        
        if r == 0:
            return 2
        elif (h // p) % 2 == 1:
            return 1
        else:
            return 0
            