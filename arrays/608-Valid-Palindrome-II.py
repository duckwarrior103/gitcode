"""
680. Valid Palindrome II 
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Examples) 
can_remove = True
'abcdgdcdba'

- two pointers, left and right
- while loop to check for palindromes, left must be < right
- track letters that do not match 
- boolean flag, can_remove = False
- if not match 

"""


class Solution:
    def check_palindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.check_palindrome(s, left+1, right) or self.check_palindrome(s, left, right-1)
            else:
                left += 1
                right -= 1
        return True


print(Solution.validPalindrome('abca'))
