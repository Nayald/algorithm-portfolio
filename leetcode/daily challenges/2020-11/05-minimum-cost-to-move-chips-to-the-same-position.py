class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        pos = [0, 0]
        for p in position:
            pos[p % 2] += 1
            
        return min(pos)