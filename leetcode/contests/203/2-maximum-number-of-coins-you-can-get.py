class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        r = piles[1]
        for i in range(3, 2 * len(piles) // 3, 2):
            r += piles[i]
        return r
        