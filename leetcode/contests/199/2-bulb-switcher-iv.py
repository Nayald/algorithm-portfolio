class Solution:
    def minFlips(self, target: str) -> int:
        action = 0
        previous = "0"
        for e in target:
            if e == "1" and previous == "0":
                action += 1
                
            if e == "0" and previous == "1":
                action += 1
            
            previous = e
        
        return action