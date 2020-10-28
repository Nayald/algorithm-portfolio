class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        max_score = score = 0
        i = 0
        j = len(tokens) - 1
        while i <= j:
            if tokens[i] <= P:
                score += 1
                max_score = max(max_score, score)
                P -= tokens[i]
                i += 1
            elif score > 0:
                score -= 1
                P += tokens[j]
                j -= 1
            else:
                break
                
        return max_score
                