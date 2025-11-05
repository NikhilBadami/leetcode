class Solution:

    EMPTY_ARRAY_CODE = "%^&empty%^&"
    JOIN_STR = "%G(X@Q)"

    def encode(self, strs: List[str]) -> str:
        """
        Use a special character or set of character to identify breaks
        between words. In this case, I will use %^& to identify breaks.
        One edge case here is an empty array. An array with a single
        value will split back into that single string, but an empty
        array will reduce to a single empty string, which then decodes back
        to an array of a single empty string. In this case, we can use
        a special character to indicate an empty array, perhaps something
        like "%^&empty%^&"

        time: O(n) --> n is the number of strings
        memory: O(m) --> m is the size of all strings
        """
        return self.JOIN_STR.join(strs) if len(strs) != 0 else self.EMPTY_ARRAY_CODE
    def decode(self, s: str) -> List[str]:
        """
        Now that I have a known special character, simply split the given
        string based on this character

        time: O(n) --> n is the number of strings
        memory: O(m) --> m is the size of all strings
        """
        return s.split(self.JOIN_STR) if s != self.EMPTY_ARRAY_CODE else []

