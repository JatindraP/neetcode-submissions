class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_str = "".join(ch for ch in s if ch.isalnum())
        alnum_str = alnum_str.lower()
        rev_alnum_str = alnum_str[::-1]
        return alnum_str == rev_alnum_str
        