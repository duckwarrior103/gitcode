'''Given a string s, return the longest 
palindromic substring in s.
'''
from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ## create a map between character and its index 
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        max_long = 1
        sequence_palindrome_map = {}
        character_indexes = defaultdict(list)
        for i in range(len(s)-1, -1, -1):
            character_indexes[s[i]].append(i)
        
        def check_palin(start, end):

            # remember to use nonlocal for python3 when we assign values to a variable out of function scope
            nonlocal max_long 
            # always check if statements and return statements: what are we trying to achieve? if the substring we're checking is already cached we can simply
            # return its lookup
            if (start, end) in sequence_palindrome_map:
                return sequence_palindrome_map[(start, end)]

            # if this is a sequence we haven't seen before, we make sure the head and tail is the same
            if s[start] == s[end]:
                ## this is the base case, an odd palindrome means length = 1, even palindrome = 2
                if end-start <= 1:
                    max_long = max(max_long, end-start+1) ## set max length 
                    sequence_palindrome_map[(start, end)] = end-start+1 ## cache it 
                    return end-start+1 ## make sure we know what to return: the length of the current palindrome substring
                else:
                    sequence_palindrome_map[((start, end))] = check_palin(start+1, end-1) + 2 if check_palin(start+1, end-1) > 0 else 0
                    max_long = max(max_long, sequence_palindrome_map[(start, end)])
                    return sequence_palindrome_map[(start, end)]
            return 0

        for i, character in enumerate(s):
            for matching_index in character_indexes[character]:
                if i == matching_index:
                    break
                check_palin(i, matching_index)
        
        if not sequence_palindrome_map or max_long == 1:
            return s[0]
        start, end = max(sequence_palindrome_map, key = sequence_palindrome_map.get)
        return s[start:end+1]

print(Solution.longestPalindrome(Solution(), "cbbd"))


'''
Notes from this question:

O(n^2) time complexity, there are n^2 combinations of substrings, and our algorithm takes basically constant time to check if it is a palindrome

Validation
- edges cases 
    - empty string 
    - string with 1 character 
    - string with 2 characters
    - string with no palindrome 

'''
