class Solution:
    def nextGreaterElement(self, n: int) -> int:
        m = [c for c in str(n)]
        i = len(m) - 2
        while i >= 0 and m[i] >= m[i + 1]:
            i -= 1
            
        if i < 0:
            return -1
        
        for j in reversed(range(i, len(m))):
            if m[i] < m[j]:
                break
                
        m[i], m[j] = m[j], m[i]
        result = int("".join(m[:i+1] + m[:i:-1]))
        return result if result < 2 ** 31 else -1