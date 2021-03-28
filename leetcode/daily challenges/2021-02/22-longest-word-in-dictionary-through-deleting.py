from collections import Counter

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        w_pointers = [0] * len(d)
        for i in range(len(s)):
            for j in range(len(d)):
                if w_pointers[j] < len(d[j]) and s[i] == d[j][w_pointers[j]]:
                    w_pointers[j] += 1
                    
        best = ""
        for w, p in zip(d, w_pointers):
            if len(w) != p or len(w) < len(best):
                continue
            
            if len(w) > len(best) or w < best:
                best = w
        
        return best
                    