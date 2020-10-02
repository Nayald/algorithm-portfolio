class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return []
        
        first = []
        d = {}
        for i, c in enumerate(S):
            if c not in d:
                d[c] = [i]
                first.append((c, i))
            else:
                d[c].append(i)

        result = []
        for e, i in first:
            if e in d:
                end = d[e][-1]
                del d[e]
                remove = []
                for k, v in d.items():
                    if i < v[0] < end:
                        end = max(end, v[-1])
                        remove.append(k)

                for k in remove:
                    del d[k]

                result.append(end-i+1)
            
        return result