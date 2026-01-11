class Solution:
    def climbStairs(self, n: int) -> int:
        """
        I'm given n, which represents the number of stairs in a stair case. I need to determine how many distinct ways I can reach the top of the
        staircase by moving 1 or two steps at a time.

        Because I can only move 1 or 2 steps at a time, these create natural base cases of 1 and 2, i.e., there is 1 way to reach the top of a
        staircase with only 1 step, and two ways to reach the top of a staircase with two steps. 

        To reach three steps, I can see that it takes 3 ways (1+1+1, 1+2, 2+1), or, the sum of the solutions to n=1 and n=2. Similarly, I can
        see that the solution for n=4 is the sum of n=3 and n=2 (5). This problem would suggest a recursive approach, but I can cache the previous
        two solutions and use iteration, arriving at a more efficient solution.

        time: O(n)
        memory: O(1) --> Only cache the previous two solutions
        """
        # Handle edge cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initialize variables to cache previous two solutions to n=1 and n=2 0-indexed
        prev_two = 1
        prev_one = 2
        soln = -1
        for i in range(2, n):
            soln = prev_two + prev_one
            prev_two = prev_one
            prev_one = soln
        return soln
        
