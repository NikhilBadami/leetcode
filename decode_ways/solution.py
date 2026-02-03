class Solution:
    def numDecodings(self, s: str) -> int:
        """
        I'm given a string where each character is a digit that corresponds to a letter of the alphabet. I need to find all valid ways to
        decode this string.

        I can start by creating a 1-indexed map of numbers mapping to characters. From there, I can consider the base cases. A string with only
        1 character can only be decoded in 1 way. A string with only 2 characters can be decoded in only 2 ways. If the string has 3 characters,
        I can either decode the string by treating the 3rd character as a single digit, or as the second digit in a two digit number using the
        i-1 indexed number as the first digit. This creates a fibonacci recurrence where the number of ways to decode a string using a given
        character is nw[i-1] + nw[i-2]

        Note that there are some edge cases. If there is a 0 in the array, it is only valid if it has a valid preceeding number, in this case, 1
        or 2. Additionally, any number that comes after 0 cannot use it and can only consider being used as a single number. Finally, we need
        to consider the case if the number formed if > 26. In all of these cases, the number of ways the string can be decoded at that point
        is just the number of ways from index - 2. The final answer is the last index of the memoization array.

        time: O(n)
        memory: O(n)
        """
        # Base cases
        if s[0] == '0':
            # No valid preceeding character is possible
            return 0
        if len(s) == 1:
            return 1
        if len(s) == 2:
            return 2 if s[1] > '0' and s[1] <= '6' and s[0] <= '2' else 1
        
        # Create array hold number of possible solutions at each character
        res = [0] * len(s)
        res[0] = 1
        res[1] = 2 if s[0] == '1' or s[0] == '2' else 1
        for i in range(2, len(s)):
            if s[i] == '0':
                # Preceeding character must be valid, otherwise the string cannot be decoded
                if s[i-1] != '1' and s[i-1] != '2':
                    return 0
                else:
                    res[i] = res[i-2]
            else:
                if s[i] >= '7':
                    res[i] = res[i-1]
                elif s[i-1] != '1' and s[i-1] != '2' or s[i-1] == '0':
                    res[i] = res[i-2]
                else:
                    res[i] = res[i-1] + res[i-2]
        return res[-1]

