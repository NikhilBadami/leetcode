class Solution:
    def numDecodings(self, s: str) -> int:
        """
        I'm given a string of numbers that can be decoded by mapping each number to an uppercase english character. The numbers could be decoded
        either as individual numbers or as part of a two digit number.

        I can either use the number only as a single number, or as part of a two digit number. How do I know if I can use the number as part
        of a two digit number? If the number is formed such that 10 <= n <= 26, then the digit can be used as a two digit number. If the number
        is 0 or the preceeding digit is > 2, the digit cannot be used as a two digit number.

        The recurrence is fibonacci. If the number can be used as part of a two digit number, the number of ways to decode the string using the
        current digit is nw[i-1] + nw[i-2]. If the digit cannot be used as part of a two digit number, the number of ways to decode does not
        change from the previous entry

        time: O(n)
        memory: O(n)
        """
        # Base case
        if s[0] == '0':
            # No valid way to decode this string
            return 0
        
        # The string can never be empty, but we handle a case where there is an empty string since it makes setting up the base cases easier
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1, len(s)):
            # Check to see if the current digit can be used as a two digit or single digit number
            # If the current character is not 0, it can definitely be used as a single character
            if s[i] == '0':
                # If the preceeding character is a 1 or a 2, the string is still valid otherwise it is invalid
                if s[i-1] == '1' or s[i-1] == '2':
                    dp[i+1] = dp[i-1]
                else:
                    return 0
            else:
                # If the digit is not 0, it can definitely be used as a single digit
                dp[i+1] += dp[i]
                if (s[i-1] == '1') or (s[i-1] == '2' and s[i] < '7'):
                    dp[i+1] += dp[i-1]
        return dp[-1]
