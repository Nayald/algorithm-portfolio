class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        r = [""] * len(s)
        for i, j in enumerate(indices):
            r[j] = s[i]
            
        return "".join(r)