class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0
        
        max_power = power = 1
        last = s[0]
        for c in s[1:]:
            if c == last:
                power += 1
                max_power = max(max_power, power)
            else:
                power = 1
                last = c
                
        return max_power