class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        I need to find out if s2 contains some ordering of the characters in s1. This means that the count of each character
        for some substring of s2 should match the count of characters in s1. Additionally, the characters should be
        continguous, i.e., if s1 = abc and s2 = eebacee then s2 contains a permutation of s1, but if it equaled eebeac, then
        it would not, because there is an e between the b and the other characters.

        I can preprocess s1 to get the count of each character in that string. Then I can process s2 using a sliding
        window to see if a permutation of s1 is a substring of s2. I iterate through s2 looking for a character that
        is in s1. If I find a character in s1, I begin expanding the window and decrement the character count in the
        frequency map. If I am able to create a window that contains all the characters with the exact counts as in s1,
        I return true as I have found what I am looking for.

        How do I shrink the window? If while iterating, I encounter a character that is not in s1, I need to recover the
        counts of each character in the string. I can do this by shrinking the window and incrementing each count for
        each character I encounter, until I reach the right pointer. Note that encountering a single character not in s1
        essentially means this window is entirely invalid, and I need to essentially discard it.

        time: O(n + m) --> n is the size of s1 and m is the size of s2. n time for counting characters in s1 and m time
        for searching for a permutation substring in s2
        memory: O(n)
        """
        # Build s1 frequency map
        s1_freqs = {}
        for c in s1:
            s1_freqs[c] = s1_freqs.get(c, 0) + 1

        # Search s2 for a permutation of s1
        i = 0
        while i < len(s2):
            if s2[i] in s1_freqs.keys():
                # Search for permutation of s1 in s2
                l, r = i, i
                while r < len(s2):
                    # Check conditions if window is invalid
                    if s2[r] not in s1_freqs.keys() or s1_freqs[s2[r]] <= 0:
                        # Shrink window and recover count of characters
                        while l < r:
                            s1_freqs[s2[l]] = s1_freqs[s2[l]] + 1
                            l += 1
                        # I do not want to re-process any characters from this window because I know that up
                        # until the character at r, ther is no possible valid substring
                        i = r
                        break
                    else:
                        # If window is valid, check if the solution has been found
                        s1_freqs[s2[r]] = s1_freqs[s2[r]] - 1
                        all_zero = True
                        for c in s1_freqs.keys():
                            if s1_freqs[c] != 0:
                                all_zero = False
                                break
                        if all_zero:
                            # Solution has been found
                            return True
                        r += 1
            else:
                i += 1
        return False

