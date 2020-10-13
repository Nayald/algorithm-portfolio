from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads:
            return 0
        
        if n == 2:
            return 1
    
        d = defaultdict(set)
        for r in roads:
            d[r[0]].add(r[1])
            d[r[1]].add(r[0])
        
        m = 0
        for k, v in d.items():
            for l, w in d.items():
                if k is not l:
                    m = max(m, len(v) + len(w) - (1 if k in w else 0))
                    
        return m
        