class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo = (sum(nums) + threshold - 1) // threshold
        hi = lo * 2
        tot = sum((x + hi - 1) // hi for x in nums)
        while tot > threshold:
            lo = hi
            hi *= 2
            tot = sum((x + hi - 1) // hi for x in nums)
            
        while lo < hi:
            mid = (lo + hi) // 2
            tot = sum((x + mid - 1) // mid for x in nums)
            if tot <= threshold:
                hi = mid
            else:
                lo = mid + 1
            
        return lo