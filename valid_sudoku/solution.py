class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        A brute force way to do this is to make 3 passes over the array:

        1: Loop over all rows and verify they are valid
        2: Loop over all columns and verify they are all valid
        3: Loop over each 3x3 sub matrix and verify they is valid

        For 3, I can set a series of ranges i.e., (0,2), (3,5), (6,8) for the rows and column to bound which sub matrices I am
        looking at. I can use a set for each search to determine if any duplicates are found.

        Since I loop over each element in the matrix at most 3 times, the time complexity reduces to 3(9*9), or 243

        time: O(1)
        memory: O(1)
        """
        # First loop over each row to verify it is valid
        for i in range(len(board)):
            dups = set()
            for j in range(len(board)):
                if board[i][j] != '.':
                    if board[i][j] in dups:
                        return False
                    else:
                        dups.add(board[i][j])

        # Next loop over the columns to check if they are valid
        for j in range(len(board[0])):
            dups = set()
            for i in range(len(board)):
                if board[i][j] != '.':
                    if board[i][j] in dups:
                        return False
                    else:
                        dups.add(board[i][j])
        
        # Finally, check each 3x3 sub board
        ranges = ((0, 2), (3, 5), (6, 8))

        # Check sub boards "col by col" i.e., top to bottom
        for r1 in ranges:
            for r2 in ranges:
                # The outer two loops define the board to search
                row_1, row_2 = r2
                col_1, col_2 = r1
                dups = set()
                for i in range(row_1, row_2+1):
                    for j in range(col_1, col_2+1):
                        if board[i][j] != '.':
                            if board[i][j] in dups:
                                return False
                            else:
                                dups.add(board[i][j])
        return True
        
