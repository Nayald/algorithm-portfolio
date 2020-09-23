class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n < 1000:
            return str(n)
        
        s = []
        while n > 1000:
            s.append(str(n)[-3:])
            n //= 1000
            
        s.append(str(n))
        return ".".join(reversed(s))