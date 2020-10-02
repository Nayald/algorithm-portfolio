class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums or k == 0:
            return 0
        
        result = 0
        prod = 1
        start = end = 0
        while end < len(nums):
            prod *= nums[end]
            while start < end and prod >= k:
                prod /= nums[start]
                start += 1
                    
            result += end - start
            end += 1
            
        return result
        