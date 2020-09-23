class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for e in arr:
            if e % 2 == 1:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        
        return False