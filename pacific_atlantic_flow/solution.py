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

        The problem with starting a search from every cell is that this solution will have O(n^2) since every cell in the grid will be processed
        up to n times. This leads to a lot of repeated work. How can I elminate this repeated work? If I start the searches from the oceans
        themselves, then every cell I can reach that respective ocean. I can start bfs using multi sources for each ocean. Pacific ocean
        sources will be left column and top row. Atlantic sources will be right column and bottom row. I iterate until both searches are
        exhausted. The solution is the intersection of the searches visited sets.

        time: O(m*n)
        memory: O(m*n)
        """
        from collections import deque
        # Create a queue and fill it with the sources for the pacific ocean
        pacific_q = deque()
        pacific_visited = set()
        # Add top row
        for j in range(len(heights[0])):
            pacific_q.append((0, j))
            pacific_visited.add((0, j))
        # Add left column
        for i in range(len(heights)):
            pacific_q.append((i, 0))
            pacific_visited.add((i, 0))
        # Get the visited set for the pacific ocean
        self._visit_cells(heights, pacific_q, pacific_visited)

        # Create queue and fill with sources for atlantic ocean
        atlantic_q = deque()
        atlantic_visited = set()
        # Add bottom row
        bot_idx = len(heights) - 1
        for j in range(len(heights[bot_idx])):
            atlantic_q.append((bot_idx, j))
            atlantic_visited.add((bot_idx, j))
        # Add right column
        right_idx = len(heights[0]) - 1
        for i in range(len(heights)):
            atlantic_q.append((i, right_idx))
            atlantic_visited.add((i, right_idx))
        self._visit_cells(heights, atlantic_q, atlantic_visited)
        return list(atlantic_visited & pacific_visited)
    
    def _visit_cells(self, heights, q, visited):
        """
        Helper function takes the heights input as well as a queue already loaded with sources and performs bfs, populating a visited set.
        Modifies visited in place
        """
        while len(q) > 0:
            # Search current set of sources
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                # Add in search cells. Since I am doing this problem in reverse, I can only add cells that are greater than or equal to the
                # current cell
                if i - 1 >= 0 and (i-1, j) not in visited and heights[i-1][j] >= heights[i][j]:
                    q.append((i-1, j))
                    visited.add((i-1, j))
                if i + 1 < len(heights) and (i+1, j) not in visited and heights[i+1][j] >= heights[i][j]:
                    q.append((i+1, j))
                    visited.add((i+1, j))
                if j - 1 >= 0 and (i, j-1) not in visited and heights[i][j-1] >= heights[i][j]:
                    q.append((i, j-1))
                    visited.add((i, j-1))
                if j + 1 < len(heights[i]) and (i, j+1) not in visited and heights[i][j+1] >= heights[i][j]:
                    q.append((i, j+1))
                    visited.add((i, j+1))
        
