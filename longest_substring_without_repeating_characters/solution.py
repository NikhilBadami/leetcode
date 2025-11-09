class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Idea is to find the longest substring without repeating characters, or, put another way, to find the longest
        substring with unique characters. I can use a sliding window to search the array, combined with a set to track
        unique characters. As I expand the window, I add characters to the set. If I find a character in the set, I begin
        shrinking the window and removing characters as I go, until all the characters in the window are unique once again.

        time: O(n)
        memory: O(n)
        """
        # Edge case if s is empty
        if len(s) == 0:
            return 0

        l, r = 0, 0
        unique_chars = set()
        max_len = -1

        while r < len(s):
            if s[r] not in unique_chars:
                unique_chars.add(s[r])
                r += 1
            else:
                max_len = max(max_len, r - l)
                while l <= r and s[r] in unique_chars:
                    unique_chars.remove(s[l])
                    l += 1
        # Final check
        max_len = max(max_len, r - l)
        return max_len
        
