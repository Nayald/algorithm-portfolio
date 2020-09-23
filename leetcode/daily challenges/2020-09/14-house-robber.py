class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        
        dp = [0] * (len(nums) + 2)
        for i in range(len(nums)):
            dp[i+2] = max(dp[i] + nums[i], dp[i+1])
            
        return dp[-1]