class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if not pattern or not str:
            return False
        
        words = str.split()
        if len(words) != len(pattern):
            return False
        
        d = {}
        s = set()
        for p, w in zip(pattern, words):
            if p not in d:
                if w not in s:
                    d[p] = w
                    s.add(w)
                else:
                    return False
            elif w != d[p]:
                return False
            
        return True