class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        I am given a number, n, which represents the number of pairs of parentheses I can work with. I need to generate all possible combinations
        of well-formed parentheses that can be generated.

        I have to start with an open parenthesis. From here I can make two choices, either add another open parenthesis or add a closed one. I
        can only add a closing parenthesis if there is a corresponding open one, otherwise I may generate an invalid solution.

        I can keep track of the number of open and close parentheses a current solution has. If the number of open parentheses exceeds the number
        of closed parentheses, I can add closed parentheses. Otherwise, I cannot. Additionally, I can only add parenthesis of any kind as long
        as the total number of each kind does not exceed n. 

        time: O(4^n) --> Length of output is 2*number of pairs
        memory: O(n) --> Recursive depth is at most n. Using arrays to build solution cuts down on memory
        """
        return self._helper(n, [], 0, 0)
    
    def _helper(self, n, cur_soln, num_open, num_closed):
        """
        Helper function that helps build solutions. Takes n, the current solution and the number of open and closed parentheses present in the
        current solution. Returns list of strings
        """
        res = []
        # Base case
        if num_open == n:
            if num_closed < n:
                # Add closing parenthesis until solution is valid
                for i in range(num_closed, n):
                    cur_soln.append(')')
                res.append(''.join(cur_soln))
                # Remove open parentheses to avoid affecting other recursion branches
                for i in range(num_closed, n):
                    cur_soln.pop()
            else:
                res.append(''.join(cur_soln))
            return res
        
        # Add open parenthesis
        cur_soln.append('(')
        res += self._helper(n, cur_soln, num_open+1, num_closed)
        cur_soln.pop()

        # Add closed parenthesis only if valid
        if num_closed < num_open:
            cur_soln.append(')')
            res += self._helper(n, cur_soln, num_open, num_closed+1)
            # This line is needed so that when the function returns, the ')' added in this call does not affect recursive calls further up
            # the call stack
            cur_soln.pop()
        
        return res

