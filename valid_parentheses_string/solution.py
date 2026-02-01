class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        I am given a string that contains only (, ) and *. I need to determine if the string is valid. The string is valid. A string is valid if
        every left parenthesis has a corresponding right parenthesis and vice versa and every left parenthesis must go before its corresponding
        right parenthesis. The '*' character can be used as a wild card, i.e., it can be treated as a single left/right parenthesis or an empty
        string.

        I can use two stacks to track the number of left parenthesis and the number of * characters along with their indices. Since each stack
        would inherently only track one type of character, each entry into the stack is just the particular index of an instance of that
        character. As I iterate through the string, if I encounter a right parenthesis, if there is a left parenthesis available or a * character
        available, I can keep iterating and remove an entry from the relevant stack. If nothing is available, the string is invalid.

        After iterating, if there are remaining left parentheses, I need to unload both the ( stack and the * stack. If there are remaining *
        characters that come *after* the ( characters, the string is valid. If there are none, the string is invalid

        time: O(n)
        memory: O(n)
        """
        left_stack = []
        wild_stack = []
        for i in range(len(s)):
            if s[i] == '(':
                left_stack.append(i)
            elif s[i] == '*':
                wild_stack.append(i)
            else:
                if len(left_stack) > 0:
                    left_stack.pop()
                elif len(wild_stack) > 0:
                    wild_stack.pop()
                else:
                    return False
        
        # If there are remaining unmatched left parenthesis, try and match them
        if len(left_stack) > 0:
            if len(left_stack) > len(wild_stack):
                return False
            while len(left_stack) > 0:
                left_i = left_stack.pop()
                wild_i = wild_stack.pop()
                if wild_i < left_i:
                    return False
        return True
        
