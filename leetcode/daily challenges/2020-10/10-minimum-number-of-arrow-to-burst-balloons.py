class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])
        result = 1
        last = points[0]
        for p in points[1:]:
            if p[0] <= last[1]:
                continue
            else:
                result += 1
                last = p
            
        return result