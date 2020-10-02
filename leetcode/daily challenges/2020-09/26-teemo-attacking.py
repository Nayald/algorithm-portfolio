class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        
        result = 0
        last = timeSeries[0]
        for i in range(1, len(timeSeries)):
            result += min(timeSeries[i] - last, duration)
            last = timeSeries[i]
            
        return result + duration