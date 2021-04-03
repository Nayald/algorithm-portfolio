from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = Counter(nums)
        return sum(k for k, v in c.items() if v == 1)