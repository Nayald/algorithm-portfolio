class Solution:
    def minOperations(self, n: int) -> int:
        l = n // 2
        if n % 2 == 1:
            return sum([2 * i for i in range(1, l + 1)])
        else:
            return sum([1 + 2 * i for i in range(0, l)])