class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr)):
            p = arr[i:i+m]
            j = i + m
            l = k - 1
            while j < len(arr):
                if arr[j:j+m] == p:
                    l -= 1
                else:
                    break
                j += m
            
            if l == 0:
                return True
            
        return False