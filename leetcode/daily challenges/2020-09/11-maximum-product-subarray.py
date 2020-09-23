class Solution:
    def maxProduct(self, nums: List[int]) -> int:      
        max_prod = float("-inf")
        left = 0
        right = 0
        prod = 1
        while right < len(nums):
            if nums[right] == 0:
                max_prod = max(max_prod, 0)
                while left < right - 1:
                    prod //= nums[left]
                    if abs(prod) < max_prod:
                        break
                        
                    max_prod = max(max_prod, prod)
                    left += 1
                
                left = right = right + 1
                prod = 1
                continue
                
            prod *= nums[right]
            right += 1
            max_prod = max(max_prod, prod)
            
        while left < len(nums) - 1:
            prod //= nums[left]
            if abs(prod) < max_prod:
                break

            max_prod = max(max_prod, prod)
            left += 1
                
        return max_prod