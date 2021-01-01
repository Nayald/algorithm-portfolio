from collections import Counter

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        e = Counter(a + b for a in A for b in B)
        f = [-(c + d) for c in C for d in D]
        result = 0
        for v in f:
            if v in e:
                result += e[v]
                
        return result