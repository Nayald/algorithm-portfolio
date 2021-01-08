class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        def swapRemove(i):
            pieces[i], pieces[-1] = pieces[-1], pieces[i]
            pieces.pop()
            
        def findPieces(v):
            for i, p in enumerate(pieces):
                if v == p[0]:
                    return i, p
                
            return -1, []
            
        i = 0
        while i < len(arr):
            j, p = findPieces(arr[i])
            if j == -1:
                return False
            
            k = 0
            while k < len(p) and p[k] == arr[i]:
                i += 1
                k += 1
                
            swapRemove(j)
            
        return True