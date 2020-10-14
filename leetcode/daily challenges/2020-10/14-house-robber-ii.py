class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) < 3:
            return max(nums)
        
        a = 0
        b = nums[0]
        for v in nums[1:-1]:
            a, b = b, max(a + v, b)
            
        c = 0
        d = nums[1]
        for v in nums[2:]:
            c, d = d, max(c + v, d)
            
        return max(b, d)