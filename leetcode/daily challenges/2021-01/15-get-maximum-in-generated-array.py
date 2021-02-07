class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        
        arr = [0] * (n + 1)
        arr[1] = result = 1
        even = True
        for i in range(2, n + 1):
            arr[i] = arr[i >> 1] if even else arr[i >> 1] + arr[(i >> 1) + 1]
            result = max(result, arr[i])
            even ^= True
            
        return result