class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        n = 1
        l = 1
        r = set()
        while (n := n % K) != 0 and n not in r:
            r.add(n)
            while n < K:
                n = n * 10 + 1
                l += 1
                
        return l if n == 0 else -1
            