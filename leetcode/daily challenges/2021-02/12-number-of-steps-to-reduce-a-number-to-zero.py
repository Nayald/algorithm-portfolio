class Solution:
    def numberOfSteps (self, num: int) -> int:
        result = 0
        while num:
            if num & 1:
                num -= 1
                result += 1
            
            num >>= 1
            result += 1
            
        return result