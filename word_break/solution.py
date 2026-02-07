class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        I'm given a string, s, and a dictionary of words and I need to see if s can be segmented in such a way that all segments are words in the
        dictionary.

        A naive solution would be to simply expand a window until the characters in the window match a word in the dictionary. Consider the
        following example though:

        s: "catsanddog", wordDict = [
            "cats", "dog", "an", "and"
        ]
        If I greedily match words, I will match the occurrence of "an" to "an" and end up with "ddog" which does not match any words. This
        algorithm would return False, which is not correct since this problem has a solution.

        A brute force solution could be to try every possible valid paritioning until one works. This would work by iterating over the string
        and once a valid parition is found, recursing into the problem again, this time with the un-partitioned string as input. If this
        partitioning fails, return to the original problem and try extending this. If another valid partitioning is found, recurse again.
        Continue doing this until either a valid partitioning is found or the end of the string is reached.

        time: O(n^2)
        memory: O(n) --> Will process input wordDict into a set
        """
        # Process wordDict into set for O(1) lookup
        dictionary = set()
        for w in wordDict:
            dictionary.add(w)
        return self._helper(s, dictionary)
        
    def _helper(self, s, dictionary):
        """
        Takes a string as input and tries to partition it. If a valid parittioning is found, it recurses again using the unpartitioned string
        as input. If the entire string can be partitioned, returns True, otherwise False
        """
        if s in dictionary:
            return True
        
        for i in range(len(s)):
            if s[0:i] in dictionary:
                # Found a valid partitioning
                can_partition = self._helper(s[i:], dictionary)
                if can_partition:
                    return True
        return False
        
