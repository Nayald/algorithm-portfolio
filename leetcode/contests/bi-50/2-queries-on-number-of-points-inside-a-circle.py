class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        def dist(a, b):
            return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
        
        result = []
        for a, b, r in queries:
            tot = 0
            for x, y in points:
                if dist((a, b), (x, y)) <= r:
                    tot += 1
                    
            result.append(tot)
            
        return result