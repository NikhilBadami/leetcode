class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        A quick low code way to do this is to reverse the matrix vertically and then transpose the result.

        time: O(n^2)
        memory: O(1)
        """
        matrix.reverse()

        # Transpose the matrix
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        

