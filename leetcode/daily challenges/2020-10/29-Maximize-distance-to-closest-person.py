class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left = [float("inf")]
        for s in seats:
            if s == 0:
                left.append(left[-1] + 1)
            else:
                left.append(0)
        
        right = [float("inf")]
        for s in reversed(seats):
            if s == 0:
                right.append(right[-1] + 1)
            else:
                right.append(0)
                
        best_dist = 0
        for i, (l, r) in enumerate(zip(left[1:], reversed(right[1:]))):
            best_dist = max(best_dist, min(l, r))
            
        return best_dist
