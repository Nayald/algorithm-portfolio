class Solution:
    def countVowelStrings(self, n: int) -> int:
        a = 1
        e = a * n
        i = e * (n + 1) // 2
        o = i * (n + 2) // 3
        u = o * (n + 3) // 4
        return a + e + i + o + u
        