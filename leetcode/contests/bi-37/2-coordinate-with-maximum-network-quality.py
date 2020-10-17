from queue import PriorityQueue

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        q = PriorityQueue()
        for current in towers:
            s = 0
            for other in towers:
                if current is other:
                    continue
                    
                d = dist(current[:2], other[:2])
                if d <= radius:
                    s -= other[-1] // (1 + d)
            
            q.put([s - current[-1]] + current[:2])
        
        return q.get()[-2:]
                
                
def dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5