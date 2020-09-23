from queue import PriorityQueue

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        result = []
        
        q = PriorityQueue()
        for i in intervals:
            q.put(i)
        q.put(newInterval)
        
        prev = q.get()
        while not q.empty():
            curr = q.get()
            if prev[1] >= curr[0]:
                prev[1] = max(prev[1], curr[1])
            else:
                result.append(prev)
                prev = curr
                
        result.append(prev)
        return result