class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        I am given a grid of heights which represent land elevations for a particular island. The island is bordered on the left and top by
        the pacific ocean and on the right and bottom by the atlantic ocean. I need to determine that if it rains on a particular cell, if water
        from that cell can flow to both oceans. Water can flow from once cell to another either north, south, east or west if the adjacent cell's
        height is less than or equal to the current cells height. I need to return a list of coordinates of cells where this is possible.

        Given the structure of the problem, I know that the top right and bottom left corners are always solutions to this problem. How can I
        determine if water flow into both oceans is possible? If I begin searching from a given cell, the success conditions are if I can reach
        a cell such that it is adjacent to one of the oceans. I know that a cell is adjacent to the pacific ocean if it is in the first column
        (j = 0) or the first row (i = 0). Additionally, I know that a cel is adjacent to the atlantic ocean if it is in the last column
        (j = len(heights[i]) - 1) or the last row (i = len(heights) - 1).

        The question now is do I start a dfs or a bfs? A depth first search could potentially explore long paths before finding a solution if
        one exists, whereas a bfs is guaranteed to find the shortest path from a cell to some point to any other point in an unweighted graph,
        which this grid is since the cost of going in any direction is the same. Therefore, I will start a bfs from each cell.

        While searching from a particular cell, I keep track of two variables, can_reach_pacific and can_reach_atlantic. If at any point, the
        search encounters points in the relevant rows/columns, I set these variables to true. If they are both true, I add the cell to the
        solution.

        One last case to consider is how to handle row and column vectors. In these cases, every cell in the vector is a solution. The
        algorithm should be able to pick up on this. 

        time: O(n^2) --> I am starting a search from every cell, meaning that it is possible I visit every cell once from every other cell
        memory: O(n) --> On any given search, I use at most n memory to track a visited set of nodes. 
        """
        # Loop through the heights array, starting a bfs from each cell
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                reach_both = self.bfs(heights, i, j, set())
                if reach_both:
                    res.append([i, j])
        return res
    
    def bfs(self, heights, i, j, visited):
        """
        Helper function takes input grid, starting cell as well as a set of visited nodes. Performs bfs starting at the given coordinates.
        Returns a boolean indicating if the cell can reach both oceans
        """
        reach_pacific, reach_atlantic = False, False
        from collections import deque
        q = deque()
        q.append((i, j))
        visited.add((i, j))
        while len(q) > 0:
            # Only process this "level" of nodes
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()

                # Check if this cell meets conditions
                # Check if cell is adjacent to pacific ocean
                if r == 0 or c == 0:
                    reach_pacific = True
                if r == len(heights) - 1 or c == len(heights[r]) - 1:
                    reach_atlantic = True
                # Check stopping condition
                if reach_pacific and reach_atlantic:
                    return True
                
                # Add new cells to search
                if r - 1 >= 0 and (r-1, c) not in visited and heights[r-1][c] <= heights[r][c]:
                    q.append((r-1, c))
                    visited.add((r-1, c))
                if r + 1 < len(heights) and (r+1, c) not in visited and heights[r+1][c] <= heights[r][c]:
                    q.append((r+1, c))
                    visited.add((r+1, c))
                if c - 1 >= 0 and (r, c-1) not in visited and heights[r][c-1] <= heights[r][c]:
                    q.append((r, c-1))
                    visited.add((r, c-1))
                if c + 1 < len(heights[r]) and (r, c+1) not in visited and heights[r][c+1] <= heights[r][c]:
                    q.append((r, c+1))
                    visited.add((r, c+1))
        return False
                
        
