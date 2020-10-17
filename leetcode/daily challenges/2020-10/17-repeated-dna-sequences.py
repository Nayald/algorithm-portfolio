class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:        
        result = set()
        subs = set()
        for i in range(len(s) - 9):
            sub = s[i:i+10]
            if sub not in subs:
                subs.add(sub)
            else:
                result.add(sub)
            
            #(subs if sub not in subs else result).add(sub) # just to remind me it is possible like this

        return result