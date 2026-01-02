class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        If I encounter a 0 while iterating through the array, I need to set that 0's row and column to 0. This is true if there is at
        least one 0 present in a particular row or column, meaning once I've found one 0, I can mark that row and column as needing
        to be updated. Since I cannot allocate additional memory, I can make this marking in the first row/column of the array. For
        example, if I find a 0 in the 2nd row and 2nd column, I can go to the first entry of the 2nd row and mark it as 0 and do 
        the same for the first entry in the first column. Then, I do a second/third pass over the array. On the second pass, for
        every column that has a 0 present, I set that entire column to 0. On the third pass, for every row that has a 0, I set every
        entry in that row to 0. Following this approach creates an overlap in the top-left corner of the matrix, however, I can
        account for this by having a separate variable track whether or not the first row needs to be 0'd out. This means that the
        top left corner of the matrix tracks whether or not the first column needs to be 0'd.

        There are some edge cases, specifically in how the first row and column are processed. Because I am using the value in the
        first row/column to determine if a particular row or column needs to be 0'd out, I need to avoid processing a row or column
        which has been 0'd out by a legimate 0 (this would make the algorithm think additional rows/columns needs to be 0'd when
        in reality they dont'). To accomplish this, I will process the rows first, specifically, the 2nd row onwards. Then, I will
        process all columns. Finally, I will process the first row. This should ensure there are no rows or columsn being 0'd
        unintentionally.

        time: O(m*n)
        memory: O(1)
        """
        # Tracks if the first row should be 0'd (i==0)
        first_row = False

        # First pass identifies rows and columns that need to be 0'd out
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    # Check to see if this is the first row
                    if i == 0:
                        first_row = True
                    else:
                        matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Next few passes set the necessary rows/columns to 0
        # First process rows 2 onwards
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                # Set row to 0
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0
        
        # Next process column
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                # Set column to 0
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        
        # Finally, check if the first row needs to be set to 0
        if first_row:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        
        return
        
