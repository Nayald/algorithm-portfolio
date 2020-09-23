from queue import PriorityQueue

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if not trips:
            return True
        
        q = PriorityQueue() 
        for num_passengers, start_location, end_location in trips:
            q.put((start_location, num_passengers))
            q.put((end_location, -num_passengers))
            
        while not q.empty():
            capacity -= q.get()[1]
            if capacity < 0:
                return False
            
        return True
            