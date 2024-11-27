"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise

- do preprocessing on string, .lower(), filter by lambda 
- check palindrome

"""


class Solution:
    def to_alpha_numeric_string(s: str) -> str:
        return ''.join(c for c in s if c.isalnum())

    def check_palindrome(s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        s = self.to_alpha_numeric_string(s)
        s = s.lower()
        return self.check_palindrome(s)
