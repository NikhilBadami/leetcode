class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        I need to find if a permutation of s1 exists in s2. Basically, I need to find a substring in s2 that has the same
        characters with the same frequencies of s1, in other words, an anagram of s1. I can pre-process s1 to find out
        what characters are in s1 along with their frequencies. I know that the substring will be len(s1), so I can use a
        window of this size to scan through s2 and check if this window contains an anagram of s1.

        The straight forward way to do this is for each window in s2, calculate its frequencies and compare this frequency
        map to that of s1. If n is the size of s1 and m is the size of s2, I will scan a window of size m up to n times
        to determine if a permutation of s1 exists in s2. This has a runtime of nm.

        I can make this run faster. I can create a window in s2 and calculate its frequencies. For both this window and s1,
        I make the size of the map 26, i.e., I include a count for every possible letter in the alphabet instead of just
        the letters that exist in s1. Then, for each window, I simply update the counts of the letters at the left and
        right pointers, and then perform an equality check between the two maps. This equality check takes O(26) = O(1)
        time and I perform this check at most m times.

        time: O(m) --> m is the size of s2
        memory: O(1) --> technically O(52)
        """
        # Check if s1 > s2:
        if len(s1) > len(s2):
            return False
        # Create map in s1 of character frequencies
        import string
        s1_freqs = {}
        for c in string.ascii_lowercase:
            s1_freqs[c] = 0
        for c in s1:
            s1_freqs[c] = s1_freqs[c] + 1
        
        # Create a window in s2 and initially pre-process it in the same way as s1
        l, r = 0, len(s1) - 1
        window_freqs = {}
        for c in string.ascii_lowercase:
            window_freqs[c] = 0
        for i in range(l, r+1):
            window_freqs[s2[i]] = window_freqs[s2[i]] + 1
        
        # Check if permutation exists in s2
        while r < len(s2):
            if window_freqs == s1_freqs:
                return True
            window_freqs[s2[l]] = window_freqs[s2[l]] - 1
            l += 1
            r += 1
            if r >= len(s2):
                break
            window_freqs[s2[r]] = window_freqs[s2[r]] + 1

        return False
