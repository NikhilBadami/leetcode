class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        I'm given a string as input and I need to partition it such that every partition of the string is a palindrome. Note that if the input
        itself is a palindrome, that counts as a valid partition.

        What if instead of splitting the string, I expand the window on recursive calls? On the top level, I expand the window to be of size
        1 character. If this window is a valid palindrome, I add the partition and recurse. On the recursion, I expand the window one more
        character. If this string is not a palindrome, I return and move the left pointer up one therefore shrinking the window.
        """
        if len(s) == 1:
            return [[s[0]]]
        res = []
        self._helper(s, 0, 0, [], res)
        return res
    
    def _helper(self, s, l, r, res, global_res):
        """
        Helper function takes string, current window pointers and running solution and global solution.
        """
        # Base cases
        if r == len(s):
            global_res.append(res.copy())
        
        # Expand the window by 1 and check if the window is a palindrome
        while r < len(s):
            r += 1
            if not self._is_palindrome(s[l:r]):
                l += 1
            res.append(s[l:r])
            self._helper(s, l, r, res, global_res)
        
    
    def _is_palindrome(self, s):
        """
        Checks if a string is a palindrome. Returns true if it is, false otherwise
        """
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
        return True
        
