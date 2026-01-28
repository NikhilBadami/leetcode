class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Hint: You are not building palindromic substrings you are partitioning the string. If you find a valid palindromic sub-string, how does
        this affect the recursion? Where should you start searching in the recursion?

        I am given a string and I need to return all possible splits of the string such that each split sub-string is a valid palindrome. The
        most straightfoward way to do this is to check all possible splits of the original string, and then all possible splits of every sub-
        string which guarantees looking at all possible sub-strings. If a valid palindrome is found, I continue searching by treating everything
        that comes after the valid palindrome as the subsequent string to search. Note that I am not building palindromes I am partitioning
        the string into palindromes (if possible). This means if I find a valid palindrome, I don't need to continue building on it I can just
        add it to the running solution.

        time: O(n*2^n) --> At each character I choose to either split or not split at that character. Additionally, I need to check if each
                           sub-string is a palindrome which takes n time in the worst case
        memory: O(n) --> I am storing each sub-string I find and the recursion stack is at most n
        """
        global_res = []
        self._helper(s, 0, [], global_res)
        return global_res
    
    def _helper(self, s, l, res, global_res):
        """
        Helper function that partitions the given string. Any valid palindromes found are store in res. If the current string
        is empty, res is added to global_res, which is updated in place
        """
        if l >= len(s):
            global_res.append(res.copy())
        
        # Partition string
        for i in range(l+1, len(s)+1):
            sub_str = s[l:i]
            if not self._is_palindrome(sub_str):
                continue
            res.append(sub_str)
            self._helper(s, i, res, global_res)
            res.pop()
        
    def _is_palindrome(self, s):
        """
        Helper function checks if the given string is a palindrome
        """
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        
        
