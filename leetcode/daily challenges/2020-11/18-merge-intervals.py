from queue import PriorityQueue

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        inters = PriorityQueue()
        for i in intervals:
            inters.put(i)
            
        r = []
        prev = inters.get()
        while not inters.empty():
            curr = inters.get()
            #print(prev, curr)
            if prev[1] >= curr[0]:
                curr[0] = prev[0]
                curr[1] = max(curr[1], prev[1])
            else:
                r.append(prev)
            
            prev = curr
                
        r.append(prev)
        return r