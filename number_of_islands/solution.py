class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        DFS through grid starting at found 1's. As I search, change processed 1s to -1 to avoid double processing.
        Run DFS within outer loop. Outer loop will start a DFS at each 1 it finds. DFS runs until all 1s reachable
        either horizontally or vertically (but not diagonally) are processed, defining one island.

        time: O(nm) where n and m are the dimensions of the grid
        memory: O(nm)
        """
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.search(grid, i, j)
                    num_islands += 1
        return num_islands
    
    def search(self, grid: List[List[str]], i, j) -> None:
        """
        Helper function that helps search for islands. Takes a position within the grid and begins searching
        from there
        """
        # Terminal conditions
        if i < 0 or i >= len(grid):
            return
        if j < 0 or j >= len(grid[i]):
            return
        if grid[i][j] == '0' or grid[i][j] == '-1':
            return

        # Change current square to processed
        grid[i][j] = '-1'

        # Check surrounding squares
        # Top
        self.search(grid, i+1, j)
        # Right
        self.search(grid, i, j+1)
        # Bottom
        self.search(grid, i-1, j)
        # Left
        self.search(grid, i, j-1)

        return
        
