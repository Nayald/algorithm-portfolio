class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        result = 0
        durations = [0] * 60
        for t in time:
            t %= 60
            result += durations[(60 - t) % 60]
            durations[t] += 1
                
        return result
                