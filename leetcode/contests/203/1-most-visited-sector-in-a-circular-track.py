from queue import PriorityQueue

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        k = [0] * n
        for i in range(1, len(rounds)):
            s, e = rounds[i-1] - 1, rounds[i] - 1
            while s != e:
                k[s] += 1
                s = (s + 1) % n
                
        k[s] += 1
                
        q = PriorityQueue()
        for i, e in enumerate(k):
            q.put((-e, i + 1))
        
        e = q.get()
        v = e[0]
        r = [e[1]]
        while not q.empty():
            e = q.get()
            if e[0] == v:
                r.append(e[1])
                
        return r