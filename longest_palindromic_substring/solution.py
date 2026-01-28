class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Naive approach would be to check every substring and then check that every substring is a palindrome or not. In the worst case scenario,
        this is an O(n^3) solution (O(n^2) to check every possible sub-string and an additional O(n) to check if that substring is a palindrome
        which must be done for every substring). 

        The repeated work here is checking if a substring is a palindrome, which is done in O(n) time, but it can be reduced to O(1) time if I
        change how I check for palindromes. Instead of starting at the end of the string, I can start in the center and expand outwards.
        The algorithm still runs in O(n) time but I can expand and check if a string is a palindrome at the same time.

        This changes the question to what is the longest palindromic substring that can be formed using the given character as the center of
        the palindrome. I need to also handle an edge case where using only a single character can lead to only considering substrings of odd
        length. To handle even length substrings as well, I also consider the case where both the current character and the character in the
        subsetquent index form the center of the substring. While expanding, if one pointer cannot expand, the check ends.

        time: O(n^2)
        memory: O(n)
        """
        self.res = ""
        self.max_len = 0

        # Start iteration from char 1 and end at the second to last character. This is because the first/last character cannot be the center of
        # a palindrome (they can only be expanded in one direction)
        for i in range(len(s)):
            # Expand using only current index as center
            l, r = i, i
            self.expand_palindrome(s, l, r)
            # Expand using both current and adjacent character as center
            l, r = i, i+1
            self.expand_palindrome(s, l, r)
        return self.res
    
    def expand_palindrome(self, s, l, r):
        """
        Helper function to expand the palindrome in s. Returns size of the palindrome and the left and right pointers
        """
        while l >= 0 and r < len(s) and s[l] == s[r]:
            cur_len = (r - l) + 1
            if cur_len > self.max_len:
                self.max_len = cur_len
                self.res = s[l:r+1]
            l -= 1
            r += 1

