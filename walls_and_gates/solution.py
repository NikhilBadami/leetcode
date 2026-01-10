class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        I'm given an mxn matrix with three values representing either water, land or a treasure
        chest. I need to find the distance of each land cell from its nearest treasure chest.

        I can start a breadth first search from each treasure cell. The values put in the queue
        will be a tuple of (cell_val, distance) and the distance will be updated only if it is
        less than the current distance of the cell. I maintain a visited set so that individual
        searches do not process a given cell multiple times. This ensures that cells are
        processed "level by level" and that the same distance is passed to each cell on the same
        level.

        time: O(t) --> t is the number of chests in the grid
        memory: O(m*n) --> worst case if every land cell is reachable from every other land cell
                           all are stored in visited set
        """
        from collections import deque
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    visited = set()
                    self.bfs(grid, i, j, visited)
        
        return
    
    def bfs(self, grid, i, j, visited):
        """
        Helper function to run a bfs starting from the given cell. Modifies the grid in place
        """
        distance = 0
        q = deque()
        q.append((i, j, distance))
        while len(q) != 0:
            # Get size of "level" in queue
            size = len(q)
            for _ in range(size):
                # Process current cell. Only update if it is land. Note that the search is
                # initialized with the treasure cell
                if grid[i][j] > 0:
                    grid[i][j] = min(grid[i][j], distance)
                    visited.add((i, j))
                # Process each neighbor cell. Only add land cells to q
                i, j, distance = q.popleft()
                if i - 1 >= 0 and grid[i-1][j] > 0 and (i-1, j) not in visited:
                    q.append((i-1, j, distance + 1))
                if i + 1 < len(grid) and grid[i+1][j] > 0 and (i+1, j) not in visited:
                    q.append((i+1, j, distance + 1))
                if j - 1 >= 0 and grid[i][j-1] > 0 and (i, j-1) not in visited:
                    q.append((i, j-1, distance + 1))
                if j + 1 < len(grid[i]) and grid[i][j+1] > 0 and (i, j+1) not in visited:
                    q.append((i, j+1, distance + 1))
        
