from functools import lru_cache

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        @lru_cache
        def champagneFrom(i, j):
            # what is above the cup at the top is the champagne we poured
            if i < 0:
                return poured
            
            # if we are outside the tower
            if j < 0 or j > i:
                return 0
            
            # return the sum of half the overflow of the 2 cups above minus capacity
            # max is for cups that will not be filled, else it will result with a negative number (in my mind it is like if the cups want to suck the champagne below or something like that)
            return max(0, 0.5 * (champagneFrom(i-1, j-1) + champagneFrom(i-1, j)) - 1)
        
        # min is because we don't care about overflow for this one but only how much it contains
        return min(1, 0.5 * (champagneFrom(query_row-1, query_glass-1) + champagneFrom(query_row-1, query_glass)))
