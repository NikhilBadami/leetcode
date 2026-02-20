class Solution:
    """
    I need to implement two methods: encode and decode. Encode takes a list of strings and
    encodes them into a single string. Decode then takes that string and splits it back
    into the original set of strings.

    The first thing that comes to mind is to use some kind of special string sequence. This
    is not robust, however, since the possible input includes all ASCII characters. How
    can I make the encoding unique to the input?

    One way to make it unique to the input is to encode the length of each string followed
    by a special separator. For example, given the input ['apple', 'orange'], I could
    encode it as 5#apple6#orange. This way when I encounter a number followed by a #
    character, I know that the next n digits correspond to a string.
    """
    def __init__(self):
        self.separator = "#"

    def encode(self, strs: List[str]) -> str:
        """
        Iterate over the list input and join each string into a single string.

        time: O(n)
        memory: O(n)
        """
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append(self.separator)
            res.append(s)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        """
        Iterate through the string. Whenever a number followed by the separator is found,
        check the next n characters after the separator as the next word int he sequence.

        time: O(n)
        memory: O(n)
        """
        res = []
        nums = "0123456789"
        i = 0
        while i < len(s):
            if s[i] in nums:
                start = i
                while s[i] in nums:
                    i += 1
                if s[i] == self.separator:
                    n = int(s[start:i])
                    res.append(s[i+1:i+1+n])
                    i += (1 + n)
                else:
                    i += 1
            else:
                i += 1
        return res


