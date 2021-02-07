class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = 1
        i = 2
        while i <= n:
            result <<= i.bit_length()
            result += i
            result %= 1000000007
            i += 1
            
        return result 
            
        