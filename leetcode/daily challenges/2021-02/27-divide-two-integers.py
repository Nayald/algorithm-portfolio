class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        result = 0
        while dividend >= divisor:
            shift = 0
            while (divisor << shift + 1) <= dividend:
                shift += 1
                
            dividend -= divisor << shift 
            result += 1 << shift
            
        return min(-result if sign else result, 2 ** 31 - 1)