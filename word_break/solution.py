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

        Another way to approach this problem would be to iterate backwards and try and see if I can create substrings based on the words in
        the dictionary. For example, starting at the end, for every character I test to see if 1: the length of that character to the end is
        in bounds and 2: if the index after that addition can be segmented. If it can, then this index can be segmented as well. The base case
        is 1 index after the end of the string (so s[i:] == True)

        time: O(ndw) --> n is the size of the string, d is the number of words in the dictionary, w is the length of the longest word in the 
                         dictionary
        memory: O(n)
        """
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s), -1, -1):
            for w in wordDict:
                if s[i:i+len(w)] == w and (i + len(w) <= len(s)):
                    dp[i] = dp[i+len(w)]
                    if dp[i]:
                        break
        return dp[0]

