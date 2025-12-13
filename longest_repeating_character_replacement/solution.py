class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Given a string, I need to find the longest substring with only one letter. I am allowed to replace up to k
        character in my sub-string in order to achieve this. I don't need to literally replace the characters, I just need
        to know how many replacements I can do. I know that I can find maximal sub-strings using a sliding window. As I
        expand the window, I only need to know how many replacements are left. When I run out of replacements, I need
        to start shirking the window.

        How do I shrink the window? In my window, I should maintain a count of the frequency of each character. As
        I expand the window, I check to see if window_size - most_freq_char_count >= k. This is a way of checking if
        I have enough replacements to make the other characters in the window match the most frequent character. If
        I can, then the window is valid and I can keep expanding. If this condition fails, I start shrinking the window
        until the condition is true again.

        time: O(n)
        memory: O(n)
        """
        freqs = {}
        l, r = 0, 0
        max_len = 0

        while r < len(s):
            freqs[s[r]] = freqs.get(s[r], 0) + 1
            window_size = (r - l) + 1
            most_freq_char_count = freqs[max(freqs, key=freqs.get)]
            if window_size - most_freq_char_count <= k:
                max_len = max(max_len, window_size)
            else:
                # Shrink window
                while not (window_size - most_freq_char_count <= k) and l < r:
                    freqs[s[l]] = freqs[s[l]] - 1
                    l += 1
                    most_freq_char_count = freqs[max(freqs, key=freqs.get)]
                    window_size = (r - l) + 1
            # Expand window
            r += 1
        return max_len
        
