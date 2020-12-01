class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        s = set()
        def helper(i):
            if not (0 <= i < len(arr)) or i in s:
                return False
            
            if arr[i] == 0:
                return True
            
            s.add(i)
            return helper(i - arr[i]) or helper(i + arr[i])
        
        return helper(start)