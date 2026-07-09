class Solution:
    def isPalindrome(self, s: str) -> bool:

        p1 = 0 
        p2 = len(s) - 1

        while p1 < p2 :
            while not self.isAlphaNumeric(s[p1]) and p1 < p2:
                p1 += 1
            while not self.isAlphaNumeric(s[p2]) and p1 < p2:
                p2 -= 1
            
            if s[p1].lower() != s[p2].lower():
                return False 
            p1 += 1
            p2 -= 1
        return True 

    def isAlphaNumeric(self,chr):
        return (ord('a') <= ord(chr) <= ord('z')) or ord('A') <= ord(chr) <= ord('Z') or (ord('0') <= ord(chr) <= ord('9')) 
        