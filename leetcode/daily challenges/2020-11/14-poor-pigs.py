import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return math.ceil(math.log(buckets) / math.log(1 + (minutesToDie + minutesToTest - 1) // minutesToDie))
        