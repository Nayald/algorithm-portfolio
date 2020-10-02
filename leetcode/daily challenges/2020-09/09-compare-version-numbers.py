class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))
        #print(v1,v2)
        
        i = j = 0
        while i < len(v1) or j < len(v2):
            a = v1[i] if i < len(v1) else 0
            b = v2[j] if j < len(v2) else 0
            
            i += 1
            j += 1
            #print(a, b)
            if a == b:
                continue
            elif a > b:
                return 1
            else:
                return -1
            
        return 0