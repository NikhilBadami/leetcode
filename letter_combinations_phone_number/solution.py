class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        I'm given a string of digits that represent numbers on a phone. Each digit maps to a set of characters. I need to determine all possible
        letter combinations the string could represent.

        The brute force way to do this would be to start at the first digit and for every letter the digit maps to, recursively build strings.
        Since each letter will map to at most 4 characters, the time complexity is O(4^n). To map each digit to a set of letters, I will use a
        map that has size O(26) or O(1).

        time: O(4^n)
        memory: O(n) --> Recursive call stack
        """
        # Create map of characters
        chars = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        # Iterate through each character in digit and start building strings
        res = []
        self._helper(digits, chars, 0, [], res)
        return res
    
    def _helper(self, digits, chars, i, cur_str, res):
        """
        Helper function to build solutions. Takes the input digits string, a map of digits to characters, the current index in digits, the
        current string and the global result. Modifies the result in place and returns nothing. Note cur_str is an array until it is added
        to the global result to avoid excessive memory usage.
        """
        if i >= len(digits):
            # Full solution available
            res.append("".join(cur_str))
            return
        
        # Loop through the characters available for the current digit
        for c in chars[digits[i]]:
            cur_str.append(c)
            self._helper(digits, chars, i+1, cur_str, res)
            cur_str.pop()
        
        return

