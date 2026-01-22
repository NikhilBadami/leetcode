class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        I am given a number, n, which represents the number of pairs of parentheses I can work with. I need to generate all possible combinations
        of well-formed parentheses that can be generated.

        I have to start with an open parenthesis. From there, I have two options: either I can add another open parenthesis if I still have the
        budget to do so (i.e., n > 0) or I can close the current parenthesis. I can also use a tracker to keep track of how many unclosed
        parenthesis I have. Once I have exhausted my budget of open parenthesis, I can reference this counter to determine how many closing
        parenthesis I need to add.

        time: O(2^n) --> For each parenthesis pair, I can choose to add an open parenthesis or close an existing one. I can do this for all n
                         pairs.
        memory: O(2^n) --> Need to generate all intermediate solutions
        """
        return self._helper("(", n-1, 1)
    
    def _helper(self, cur_soln: str, n: int, num_open: int) -> List[str]:
        """
        Helper function that returns a list of solutions found. Takes n, the number of available pairs, and num_open, a counter which counts how
        many un-paired open parenthesis there are in the current solution.
        """
        soln = []
        if n == 0:
            # Out of parenthesis pairs
            # Check if there are un-closed parentheses. If so, add relevant number of closing parentheses
            for i in range(num_open):
                cur_soln += ')'
            soln.append(cur_soln)
            return soln
        
        # Add an open parenthesis to the current solution
        soln += self._helper(cur_soln + '(', n-1, num_open+1)
        # Add a closed parenthesis to the current solution
        soln += self._helper(cur_soln + ')(', n-1, num_open)

        return soln
        
