class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = {}
        for (x, y), v in zip(equations, values):
            if x not in d:
                d[x] = {}
            d[x][y] = v
            
            if y not in d:
                d[y] = {}
            d[y][x] = 1 / v
        
        def find_path(x, y, path=set()):
            if x == y:
                return 1
            
            s = set(d[x]) - path
            if not s:
                return float("-inf")
            
            return max([d[x][k] * find_path(k, y, path | {x}) for k in s])
            
            
        result = []
        for x, y in queries:
            if x not in d or y not in d:
                result.append(-1)
                continue
            
            r = find_path(x, y)
            result.append(r if r != float("-inf") else -1) 
                      
        return result
