class Solution:
    def countVowelStrings(self, n: int) -> int:
        v = [1] * 5
        for _ in range(1, n):
            for i in range(1, len(v)):
                v[i] += v[i - 1]
            
        return sum(v)