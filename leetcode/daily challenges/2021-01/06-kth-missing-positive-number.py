class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 0
        n = 1
        while i < len(arr) and k:
            if n == arr[i]:
                i += 1
            else:
                k -= 1
                
            n += 1
            
        return n + k - 1