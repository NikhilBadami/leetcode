class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        The question is asking us to print all elements in the matrix in spiral order starting at the top left corner.
        This can be accomplished by tracking the corners of the matrix, and interating until the top and bottom corners
        on each size of the matrix cross each other. We loop through each row and column, and then move each corner
        inwards.
        
        time: O(nm) where n and m are the dimensions of the matrix
        memory: O(nm) --> used to store the output
        """
        # Define corners
        top_left = [0, 0]
        bottom_left = [len(matrix)-1, 0]
        top_right = [0, len(matrix[0])-1]
        bottom_right = [len(matrix)-1, len(matrix[0])-1]

        # Iterate through matrix
        res = []
        while self.__check_conditions__(top_left, bottom_right):
            # Check edge case where all corners are the same square
            if top_left == top_right == bottom_right == bottom_left:
                res.append(matrix[top_left[0]][top_left[1]])
                break
            # Loop top row.
            for i in range(top_left[1], top_right[1]):
                row = top_left[0]
                res.append(matrix[row][i])
            # Loop right column.
            for i in range(top_right[0], bottom_right[0]):
                col = top_right[1]
                res.append(matrix[i][col])
            # Loop bottom row
            for i in range(bottom_right[1], bottom_left[1], -1):
                row = bottom_right[0]
                res.append(matrix[row][i])
            # Loop left column
            for i in range(bottom_left[0], top_left[0], -1):
                col = bottom_left[1]
                res.append(matrix[i][col])
            # Update corners
            top_left = [top_left[0]+1, top_left[1]+1]
            bottom_left = [bottom_left[0]-1, bottom_left[1]+1]
            top_right = [top_right[0]+1, top_right[1]-1]
            bottom_right = [bottom_right[0]-1, bottom_right[1]-1]
        
        return res
        
    def __check_conditions__(self, top_left, bottom_right):
        """
        Checks conditions to end looping. Only need to check one pair of diametricaly opposite corners. Checks to see
        if they have passed each other
        """
        if top_left[0] > bottom_right[0] and top_left[1] > bottom_right[1]:
            return False
        return True
        
