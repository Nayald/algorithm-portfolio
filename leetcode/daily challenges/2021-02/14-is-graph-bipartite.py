class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        d = {}
        for i ,e in enumerate(graph):
            d[i] = set(e)
              
        seen = set()
        AB = [set(), set()]
        pos = 1
        while len(seen) < len(d):
            start = list(d.keys() - seen)[0]
            AB[pos ^ 1].add(start)
            seen.add(start)
            #print(start)
            next = d[start]
            while next:
                AB[pos] |= next
                seen.update(next)
                new_next = set()
                for n in next:
                    if AB[pos] & d[n]:
                        print(AB[pos] & d[n])
                        return False
                    
                    new_next.update(d[n] - seen)

                next = new_next
                pos ^= 1
            
        #print(AB)
        return True