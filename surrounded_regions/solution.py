class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        I am given a board and I need to "capture" all regions on the board that are surrounded. A region is defined by a set of O's that are
        connected either horizontally or vertically. A region is surrounded if it is surrounded by X cells and none of the region cells are one
        the boards edge, i.e., the edge of the board does not count as an X.

        I can identify regions using depth first search starting from any found O. The depth first search will search in all valid directions
        until it either finds a board edge or finds an X. If all directions of the search find an X, the region is surrounded and I can go back
        and replace all region cells with an X, marking it as captured. If at any point I encounter a region edge, the region cannot possibly
        be surrounded. This also means any O's encountered along the edges of the board, by definition, cannot be surrounded.

        Would it be easier to search backwards starting from any region connected to an edge? In other words, I know that any region that can
        find an edge by definition cannot be surrounded. If I search along the edges first for any region cells, I can mark all cells that can
        reach this edge as ineligible to be surrounded. Then, any remaining O cells must by definition be able to be surrounded. I can mark
        ineligible cells with I.

        After marking all ineligible cells, I iterate through the board and chance all remaining O cells to X. Finally, I do one more pass over
        the board and change any I cells back to O and return.

        time: O(m*n) --> All cells are processed at most 3 times
        memory: O(1) --> The board is modified in place
        """
        # Perform initial DFS to change all border O cells and any connected cells to I
        # Check top row
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                self._dfs(board, 0, j)
        # Check right column
        col = len(board[0]) - 1
        for i in range(len(board)):
            if board[i][col] == 'O':
                self._dfs(board, i, col)
        # Check bottom row
        row = len(board) - 1
        for j in range(len(board[row])):
            if board[row][j] == 'O':
                self._dfs(board, row, j)
        # Check left column
        for i in range(len(board)):
            if board[i][0] == 'O':
                self._dfs(board, i, 0)
        
        # Iterate through the board and change any remaining O's to X's
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        # Finally, iterate over the board one last time and change any I's to O's
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'I':
                    board[i][j] = 'O'
    
    def _dfs(self, board, i, j):
        """
        Performs depth first search starting at the given (i, j) coordinates. Changes any encountered 'O' cell to an I
        """
        if i < 0 or i >= len(board):
            return
        if j < 0 or j >= len(board[i]):
            return
        if board[i][j] == 'X' or board[i][j] == 'I':
            return
        
        board[i][j] = 'I'
        # Search horizontally and vertically
        self._dfs(board, i-1, j)
        self._dfs(board, i+1, j)
        self._dfs(board, i, j-1)
        self._dfs(board, i, j+1)
        
