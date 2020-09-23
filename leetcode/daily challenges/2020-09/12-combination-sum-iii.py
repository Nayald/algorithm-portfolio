class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        tmps = []
        for i in range(1, 10):
            for j in range(len(tmps)):
                s, r = tmps[j]
                s += i
                if len(r) == k - 1 and s == n:
                    result.append(r + (i,))
                elif len(r) < k and s <= n:
                    tmps.append((s, r + (i,)))
                    
            tmps.append([i, (i,)])
            
        return result