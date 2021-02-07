class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        #s = []
        #k -= n
        #while n:
        #    c = min(25, k)
        #    s.append(chr(ord("a") + c))
        #    k -= c
        #    n -= 1
        #    
        #return "".join(s[::-1])
        k -= n
        z = k // 25
        y = k % 25
        if y:
            return "a" * (n - z - 1) + chr(ord("a") + y) + "z" * z
        else:
            return "a" * (n - z) + "z" * z