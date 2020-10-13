class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        
        counta = [0] * 26
        countb = [0] * 26
        diff = 0
        for a, b in zip(A, B):
            if a != b:
                diff += 1
                if diff > 2:
                    return False
            
            counta[ord(a) - ord("a")] += 1
            countb[ord(b) - ord("a")] += 1
            
        return counta == countb and (diff == 2 or any([x >= 2 for x in counta]))