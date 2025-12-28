class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Similar to num islands problem difference is need to track number of 1s in this solution. I can modify the DFS as
        follows: For a given search, I use a global variable to track the number of 1's. Every valid square encountered
        increments this counter. This is then returned and updated to be the overall solution if it is greater than the
        current solution.

        time: O(m*n)
        memory: O(m*n)
        """
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    cur_area = self.dfs(grid, i, j, 0)
                    max_area = max(max_area, cur_area)
        return max_area
    
    def dfs(self, grid, i, j, cur_area):
        """
        Helper function that searches for the size of each island. Updates cur_area variable on each valid square
        """
        # Base cases
        if i >= len(grid) or i < 0:
            return cur_area
        if j >= len(grid[i]) or j < 0:
            return cur_area
        if grid[i][j] != 1:
            return cur_area
        
        # Update the current square to -1 and update counter
        grid[i][j] = -1
        cur_area += 1

        # Search clockwise starting from left
        cur_area = self.dfs(grid, i, j-1, cur_area)
        cur_area = self.dfs(grid, i-1, j, cur_area)
        cur_area = self.dfs(grid, i, j+1, cur_area)
        cur_area = self.dfs(grid, i+1, j, cur_area)

        return cur_area
        
