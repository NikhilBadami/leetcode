class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Goal is to find the longest substring without duplicat characters. In other words, the substring should only include
        unique characters. I can solve this problem using a set and a sliding window. The set keeps track of the characters
        in the window. When I encounter a duplicate character, I shrink the window and remove characters from the set
        until there are no more duplicate characters.

        time: O(n)
        memory: O(n)
        """
        max_len = 0
        if len(s) == 0:
            return max_len
        
        unique_chars = set()
        l, r = 0, 0
        while r < len(s):
            if s[r] not in unique_chars:
                unique_chars.add(s[r])
                r += 1
            else:
                max_len = max(max_len, r - l)
                while s[r] in unique_chars and l < r:
                    unique_chars.remove(s[l])
                    l += 1
        # Handle case where we get to the end of the string without encountering duplicates
        max_len = max(max_len, r - l)
        return max_len
        
