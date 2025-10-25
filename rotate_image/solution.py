class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        One way to do this is to remove one row/column and then copy each element in the remaining rows/columns
        in place. For example, we can remove the top row and then copy all the elements into their new spots,
        and then finally copy the top row (which was held out in a temp variable) into its new spot.

        An algorithm could look like this:

        Have variables tracking the top left, bottom left, top right, bottom right corners of the sub-matrix we
        are looking at. These variables will track the bounds of the portion of the matrix we are rotating and
        will move along the diagonals of the matrix. The algorithm ends when these bounds pass each other, i.e.,
        bottom right < top left.

        For each sub-matrix, we remove the top row and store it in a temp variable. We then loop over the rows and
        columns in this order: left column, bottom row, right column, with the top row being copied into the right
        column once processing is done.

        Each copy procedure will have its own loop.
        Left Column:
            Loop down the column starting at top left corner row - 1 (because the top row was removed so there
            technically isn't an element here). Loop until the pointer exceeds the bottom left corner row. Copy
            the current element into the top row starting at top right column - 1. the next element will go into
            top right column - 2 and so on.
        Bottom Row:
            Loop across the column going from bottom left colum + 1 to bottom right column. Copy the first element
            into left column at top left row + 1. Second element into top left row + 2 and so on
        Right Column:
            Loop up right column starting at bottom right corner row - 1. Copy this element into bottom right
            column - 1. Second element into bottom right column - 2 and so on
        
        Finally, Copy the top row which was previously removed into the right column starting at the top

        time: O(n^2) -> since matrix is nxn
        memory: O(1) --> Rotation is done in place
        """
        # Because the matrix is nxn, I can get the max bounds immediately
        n = len(matrix)

        # Save corners are (row, col) coordinates
        top_left = [0, 0]
        bottom_left = [n-1, 0]
        top_right = [0, n-1]
        bottom_right = [n-1, n-1]

        while not self.check_bounds(top_left, bottom_right):
            # Save the top row
            temp = matrix[top_left[0]][top_left[1]:top_right[1]+1]

            # Process the left column
            # Save the column in a variable. We are looping across rows
            row = top_left[0]
            col = top_left[1]
            offset = 1
            for i in range(top_left[0] + 1, bottom_left[0] + 1):
                matrix[row][top_right[1] - offset] = matrix[i][col]
                offset += 1
            
            # Process the bottom row
            # Save row as a variable. We are looping across columns
            row = bottom_left[0]
            col = bottom_left[1]
            offset = 1
            for i in range(bottom_left[1] + 1, bottom_right[1] + 1):
                matrix[top_left[0] + offset][col] = matrix[row][i]
                offset += 1
            
            # Process the right column
            # Save column as a variable. We are looping across rows
            row = bottom_right[0]
            col = bottom_right[1]
            offset = 1
            for i in range(bottom_right[0] - 1, top_right[0] - 1, -1):
                matrix[row][bottom_left[1] + offset] = matrix[i][col]
                offset += 1
            
            # Copy the temp row back into the right column
            temp_ctr = 0
            col = top_right[1]
            for i in range(top_right[0], bottom_right[0] + 1):
                matrix[i][col] = temp[temp_ctr]
                temp_ctr += 1
            
            # Update corners
            top_left[0] += 1
            top_left[1] += 1

            bottom_left[0] -= 1
            bottom_left[1] += 1

            top_right[0] += 1
            top_right[1] -= 1

            bottom_right[0] -= 1
            bottom_right[1] -= 1
    
    def check_bounds(self, top_left, bottom_right):
        """
        Helper function that checks to see if bounds have passed each other. Assuming the bounds are moved correctly,
        we only need to check one set of corners
        """
        # Check to see if top_left and bottom right are equal to each other or have crossed each other
        end_loop = False
        if (top_left[0] == bottom_right[0] and top_left[1] == bottom_right[1]) or (top_left[0] > bottom_right[0] and top_left[1] > bottom_right[1]):
            end_loop = True
        return end_loop
        
