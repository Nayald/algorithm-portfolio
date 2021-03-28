class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        result = 0
        while Y > X:
            if Y % 2 == 0:
                Y //= 2
            else:
                Y += 1
            
            result += 1
            
        return result + X - Y