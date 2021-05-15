class Solution:
    def sortSentence(self, s: str) -> str:
        tokens = s.split()
        l = [None] * len(tokens)
        for t in tokens:
            l[int(t[-1]) - 1] = t[:-1]
            
        return " ".join(l)