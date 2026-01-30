class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        I am given a string as and I need to return the number of palindromic substrings in it.

        I know that I can find palindromic substrings efficiently by treating the current character in the string as the center of a palindrome
        and then expanding outwards. I will need to check that each new expansion is also a palindrome, which can be done in O(n) time.
        Finally, I need to check both even and odd palindromes. This means using both the current index as the center and the current index + 1.
        For each valid palindrome I find, I increment a global counter.

        time: O(n^2)
        memory: O(1)
        """
        # Global counter
        self.num_palindromes = 0

        # Iterate through the string
        for i in range(len(s)):
            # Use only the current character as the center of the palindrome
            l, r = i, i
            self.check_palindrome(s, l, r)
            # Check using cur char and cur_char + 1 as center
            l, r = i, i+1
            self.check_palindrome(s, l, r)
        return self.num_palindromes
    
    def check_palindrome(self, s, l, r):
        """
        Checks if the substring within the bounds l and r forms a valid palindrome. If so, increments a global counter
        """
        while l >= 0 and r < len(s) and s[l] == s[r]:
            self.num_palindromes += 1
            l -= 1
            r += 1
        
