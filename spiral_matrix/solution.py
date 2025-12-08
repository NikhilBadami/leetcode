class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Hint: How are you tracking the bounds of what elements you should be iterating over?
        Can track four pointers: Left, right, top bottom. I change each pointer afer using it. For example, the first
        iteration is going from left to right (I keep the left pointer in place for this iteration since I need it for
        going right to left on the bottom row). Then I go from top to bottom in the right column. I lower the top pointer.
        Then I go from right to left on the bottom row. I move the right pointer inwards. Then I go from bottom to top.
        I increment the bottom pointer and move the left pointer over one. I then repeat the algorithm. To help solve
        edge cases, have the right and bottom pointers be out of bounds initially.

        time: O(nm) --> nxm matrix
        memory: O(nm) 
        """
        l, r, t, b = 0, len(matrix[0]), 0, len(matrix)
        res = []

        while r > l and b > t:
            # Loop top row from left to right
            for i in range(l, r):
                res.append(matrix[t][i])
            # Increment top pointer
            t += 1
            if t >= b:
                break
            
            # Loop right column from top to bottom
            for i in range(t, b):
                res.append(matrix[i][r-1])
            # Decrement right pointer
            r -= 1
            if r <= l:
                break

            # Loop bottom row from right to left
            for i in range(r-1, l-1, -1):
                res.append(matrix[b-1][i])
            # Update bottom pointer
            b -= 1

            # Loop left column from bottom to top
            for i in range(b-1, t-1, -1):
                res.append(matrix[i][l])
            # Update left pointers
            l += 1
        return res

