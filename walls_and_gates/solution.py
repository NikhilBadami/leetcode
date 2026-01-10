class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        I'm given an mxn matrix with three values representing either water, land or a treasure
        chest. I need to find the distance of each land cell from its nearest treasure chest.

        One way to do this would be to start a dfs from each land cell and find the closest
        treasure chest. This would work but means I may recurse through land cells multiple
        times if my search moves through them while searching for a treasure chest. These
        additional land cells to not have their information updated during these recursive
        calls which leads to wasted effort.

        Another way to approach the problem would be to iterate from each *treasure chest*
        Starting from each treasure chest, I run a dfs that includes a counter showing how far
        this particular part of the search is from the starting chest. For each land cell I
        encounter, I set its value to this counter. While iterating, I take the
        min(cur_value, counter) for each land cell. This way, if I start a search from another
        chest that happens to be closer to a given land cell, the cell is correctly updated.

        time: O(t) --> Because I'm starting the search from a treasure chest, I only process each
                       cell in the graph up to t times
        memory: O(m*n) --> The size of the call stack which in the worst case is the size of the
                           input grid
        """
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    # Set of tuples that tracks pairs (i,j) of visited land cells
                    visited = set()
                    # Search starting from this point
                    self._helper(grid, i-1, j, 1, visited)
                    self._helper(grid, i+1, j, 1, visited)
                    self._helper(grid, i, j-1, 1, visited)
                    self._helper(grid, i, j+1, 1, visited)
        return
    
    def _helper(self, grid, i, j, distance, visited):
        """
        Helper function to perform dfs starting from a treasure chest. Updates land cells
        with their distance from the chest that started the search. Updates grid in place
        """
        if i >= len(grid) or i < 0:
            return
        if j >= len(grid[i]) or j < 0:
            return
        if (i, j) in visited:
            return
        if grid[i][j] == -1 or grid[i][j] == 0:
            # Do not update water or chest cells
            return
        
        # Update land cells based on distance from the starting chest
        grid[i][j] = min(grid[i][j], distance)
        # visited.add((i, j))
        distance += 1
        self._helper(grid, i-1, j, distance, visited)
        self._helper(grid, i+1, j, distance, visited)
        self._helper(grid, i, j-1, distance, visited)
        self._helper(grid, i, j+1, distance, visited)

        return

        
