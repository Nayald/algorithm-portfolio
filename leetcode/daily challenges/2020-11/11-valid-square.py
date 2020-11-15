class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def square_dist(x, y):
            return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2
            
        
        
        s = list(set([square_dist(p1, p2), square_dist(p1, p3), square_dist(p1, p4), square_dist(p2, p3), square_dist(p2, p4), square_dist(p3, p4)]))
        return len(s) == 2 and (s[0] == 2 * s[1] or s[1] == 2 * s[0])