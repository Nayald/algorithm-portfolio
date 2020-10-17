class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        start = int(len(arr) * 0.05)
        end = int(len(arr) * 0.95)           
        return sum(arr[start:end]) / int(len(arr) * 0.9)