class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Hint: Consider how you are setting your max frequency and if it is calculated in all places it should
        be calculated in

        This character can be solved with a sliding window with the condition that we can make the necessary number of
        replacements within the window. This can be accomplished by tracking the count of each character in the window
        and checking to see if we can replace the less frequent characters with the most frequent characters. If we
        have window size window_size and max count max_count, the condition for the window is
        window_size - max_count <= k. If this condition is true, we can continue expanding the  window and if not, we
        need to shrink the window.

        time: O(n)
        memory: O(1)
        """
        l, r = 0, 0
        freq = {}
        res = 0

        while r < len(s):
            freq[s[r]] = 1 + freq.get(s[r], 0)

            # Check to see if the window size is invalid
            # Note that the max count is updated on each check
            while (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        return res
