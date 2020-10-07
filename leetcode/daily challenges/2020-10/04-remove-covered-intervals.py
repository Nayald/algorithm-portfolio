class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:       
        l = []
        for a in intervals:
            for b in intervals:
                if a is b:
                    continue
                if covered(a, b):
                    l.append(a)
                    break
        
        return len(intervals) - len(l)
                    
        
def covered(a, b):
    return b[0] <= a[0] and a[1] <= b[1]