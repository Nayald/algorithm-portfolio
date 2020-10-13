class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        if len(a) <= 2:
            return True
        
        if isPalindrome(a):
            return True
        
        if isPalindrome(b):
            return True
        
        m1 = 0
        while a[m1] == b[len(a) - m1 - 1]:
            m1 += 1
            
        m2 = 0
        while b[m2] == a[len(a) - m2 - 1]:
            m2 += 1
            
        return isPalindrome(a[:m1] + b[m1:]) or isPalindrome(b[:m2] + a[m2:]) or isPalindrome(a[:-m1] + b[-m1:]) or isPalindrome(b[:-m2] + a[-m2:])
        
        
def isPalindrome(s):
    stop = len(s) // 2
    i = 0
    while i < stop:
        if s[i] != s[len(s) - i - 1]:
            return False
        
        i += 1
    
    return True