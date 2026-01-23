class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        I am given a grid which contains 3 values representing either an empty cell, a fresh orange or a rotten orange. Any fresh orange that is
        4-directionally adjacent to a rotten orange will become rotten itself on the next timestemp (note, this means even one 4-directionally
        adjacent cell that is rotten will turn a fresh orange rotten). I need to determine if it is possible for all the oranges to turn rotten
        and if so, how long it will take for this to happen.

        One straightforward way to do this would be to simulate each timestep. One each timestep, iterate through the array and convert valid
        fresh oranges into rotten oranges. I can count the number of fresh oranges on each timestep. If I have a timestep where the number of
        fresh oranges doesn't change, then I know that either I've found a solution or no solution exists. To realize this, I can set newly
        rotten oranges to 3 to avoid double processing, and then post process all 3's into 2s. This would have a time complexity of O(t(mn)) where
        t is the number of timesteps needed to determine if it is possible to rot all oranges.

        Can I do better? Is it necessary to simulate every timestep? Yes, I can use a multi-source breadth first search where I start from each
        initially present rotten orange. Then, I can start searching from each rotten orange and try and reach every other orange. Each "level"
        of the search represents a timestep. On each timestep, I add each adjacent fresh orange if any exist to the queue. After popping them
        from the queue, I turn them rotten and find any fresh oranges adjacent to them. After completing the initial search, I need to iterate
        over the array to check if there are any fresh oranges. If there are not, I return how many iterations it took to rot all oranges as
        the number of timesteps, or, if a fresh orange is found, I return -1. BFS guarantees that when a cell is processed, it is being processed
        by the source closes to it.

        time: O(mn) --> Each cell will be processed 3 times. Once to get the initial sources for the BFS. Once if any cell is processed as part
                        of the BFS and once during post processing to find any remaining fresh oranges.
        memory: O(mn) --> Worst case the queue may hold all cells present in the grid
        """
        from collections import deque
        # queue takes coordinates of rotten oranges
        q = deque()

        # Initial processing to find all initially rotten oranges
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i, j))
        
        # Perform bfs from each "source" (rotten orange)
        timesteps = 0
        while len(q) != 0:
            # Get current size of q. This represents one timestep
            size = len(q)
            for _ in range(size):
                # Pop each currently rotton orange from the queue
                i, j = q.popleft()
                # Find any fresh oranges near this rotten orange. If any are found, rot them and add them to the queue
                if i-1 >= 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    q.append((i-1, j))
                if i+1 < len(grid) and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    q.append((i+1, j))
                if j-1 >= 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    q.append((i, j-1))
                if j+1 < len(grid[i]) and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    q.append((i, j+1))
            # Increment the timestep only if there were fresh oranges found
            if len(q) > 0:
                timesteps += 1
        
        # Perform a final check to see if there are any remaining fresh oranges
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        return timesteps
        
