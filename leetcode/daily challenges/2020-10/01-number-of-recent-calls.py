class RecentCounter:

    def __init__(self):
        self.count = []

    def ping(self, t: int) -> int:
        self.count.append(t)
        lo = 0
        hi = len(self.count)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.count[mid] < t - 3000:
                lo = mid + 1
            else:
                hi = mid
        
        return len(self.count) - lo


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)