class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        s = {0:0}
        sum = 0
        for i, v in enumerate(nums, start=1):
            sum += v
            s[sum] = i   
        
        result = s[x] if x in s else len(nums) + 1
        sum = 0
        for i, v in enumerate(reversed(nums), start=1):
            sum += v
            if x - sum in s:
                result = min(result, s[x - sum] + i)
            
        return result if result != len(nums) + 1 else -1