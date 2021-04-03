class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = 0
        curr = 0
        for n in gain:
            curr += n
            result = max(result, curr)
            
        return result