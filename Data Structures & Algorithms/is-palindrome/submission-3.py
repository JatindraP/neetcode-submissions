class Solution:

    def isAlphaNumeric(self, ch) -> bool:
        return (ord("A") <= ord(ch) <= ord("Z")) or (ord("a") <= ord(ch) <= ord("z")) or (ord("0") <= ord(ch) <= ord("9"))

    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) -1

        while i <= j :
            while i <= j and not self.isAlphaNumeric(s[i]):
                i += 1
            while j >= i and not self.isAlphaNumeric(s[j]):
                j -= 1

            if i <= j and s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
        
        