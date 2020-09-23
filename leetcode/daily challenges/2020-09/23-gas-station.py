class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        delta = [0] * len(gas)
        extra_gas = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            delta[i] = g - c
            extra_gas += g - c
            
        if extra_gas < 0:
            return -1
            
        for i in range(len(delta)):
            # cost more than it gives
            if delta[i] < 0:
                continue
                
            # do the trip
            j = (i + 1) % len(gas)
            s = delta[i]
            while j != i:
                s += delta[j]
                if s < 0:
                    break
                else:
                    j = (j + 1) % len(gas)
            
            if j == i:
                return i
            
        return -1