class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        s = set()
        for w in words:
            wm = []
            for c in w:
                wm.append(m[ord(c) - ord("a")])
                
            s.add("".join(wm))
            
        return len(s)