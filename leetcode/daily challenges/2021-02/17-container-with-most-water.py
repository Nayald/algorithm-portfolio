class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        
        left = 0
        right = len(height) - 1
        result = min(height[left], height[right]) * (right - left)
        while left < right:
            
            if height[left] < height[right]:
                left += 1
                h = height[left]
            else:
                right -= 1
                h = height[right]
                
            result = max(result, h * (right - left))
                    
        return result