class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        I'm given a grid that has water, land and treasure chests. I need to find the distance
        of each land cell to its closest treasure chest.

        I can use a breadth first search to find how far each land cell is from a treasure chest
        starting at each individual chest. This is because bfs operates "level by level," meaning
        that it searches all cells closest to the start first. This means that when a cell is
        encountered, it is guaranteed to be the first time.

        Because there can be multiple treasure chests, I should start the search from each
        chest simultaneously. I can do this by making a pass over the grid first and adding all
        chests to a queue. Information in the queue will be stored as tuples containing
        the position of each cell as well as its current distance from a chest. Only land and
        treasure chests will be added.

        time: O(m*n) --> Each cell will only be processed twice
        memory: O(m*n) --> Need to maintain a set of visited cells
        """
        inf = 2147483647
        from collections import deque
        q = deque()

        # Make first pass over grid to find all chests
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append((i, j, 0))

        # Process queue, finding all reachable land cells and updating their distance from their
        # respective chests
        visited = set()
        while len(q) != 0:
            # Get size of current "level"
            size = len(q)
            for _ in range(size):
                # Every cell in this level has same distance from source
                i, j, distance = q.popleft()
                # Don't process visited nodes
                if (i, j) in visited:
                    continue
                # Update cell distance from source and add to visited set
                grid[i][j] = min(grid[i][j], distance)
                visited.add((i, j))

                # Process adjacent cells provided they are land
                if i + 1 < len(grid) and grid[i+1][j] == inf:
                    q.append((i+1, j, distance + 1))
                if i - 1 >= 0 and grid[i-1][j] == inf:
                    q.append((i-1, j, distance + 1))
                if j + 1 < len(grid[i]) and grid[i][j+1] == inf:
                    q.append((i, j+1, distance + 1))
                if j - 1 >= 0 and grid[i][j-1] == inf:
                    q.append((i, j-1, distance + 1))

        
