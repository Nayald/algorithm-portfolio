from collections import Counter, defaultdict

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if not nums:
            return 0
                
        d = defaultdict(int)
        result = 0
        for n in nums:
            d[n] += 1
            if {n + 1, n - 1} & d.keys():
                result = max(result, c[n] + c[n + 1])
                
        return result