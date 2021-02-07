from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result = 0
        d = defaultdict(int)
        for n in nums:
            if d[k - n] >= 1:
                result += 1
                d[k - n] -= 1
            else:
                d[n] += 1
                
        return result