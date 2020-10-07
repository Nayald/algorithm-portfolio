from collections import defaultdict

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:       
        # dict of b = k + a
        d = defaultdict(int)
        for v in nums:
            d[v + k] += 1
        
        if k == 0:
            return len([k for k, v in d.items() if v > 1])
        
        seen_pair = set()
        for v in nums:
            if v in d:
                pair = (v - k, v)
                if pair not in seen_pair:
                    seen_pair.add(pair)
        
        return len(seen_pair)