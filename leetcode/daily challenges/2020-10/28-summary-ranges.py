class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        result = []
        range = [nums[0]]
        for v in nums[1:]:
            if v == range[-1] + 1:
                range.append(v)
            else:
                if len(range) > 1:
                    result.append(str(range[0]) + "->" + str(range[-1]))
                else:
                    result.append(str(range[0]))
                
                range = [v]
        
        if len(range) > 1:
            result.append(str(range[0]) + "->" + str(range[-1]))
        else:
            result.append(str(range[0]))
        
        return result