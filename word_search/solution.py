class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        I'm given a grid, board, which contains characters. I am also given a string, word, and I need to see if word exists in the board.
        The word exists in the board if it can be constructed by sequentially adjacent cells, where adjacent cells are defined as being
        neighboring either horizontally or vertically.

        I can only start building a candidate solution from the starting character of the word. If at any point while searching I find an
        invalid character, where invalid in this case means a letter note in word, I end the search. Given that the problem structure reflects
        searching as deeply as possible from a starting character, this suggests DFS starting whenever the first letter of word is found in
        the board. I perform dfs from the first character; if I am able to reach the final character, I return true. If at any point I find an
        invalid character, I return false.

        I will need to potentially start the dfs from every cell in the board. At most, I can start 4 dfs searches that can potentially explore
        the entire board. This means the overall time complexity is 4^n.
        Finally, I need to maintain a set of visited cells for each search to avoid visiting cells multiple times. This also takes up
        potentially n memory but doesn't change the overall complexity. Note that I will need to start 4 separate searches. This is because
        using only a single search means using only a single visited set. This means that if one search reaches a valid letter out of order,
        that cell will not be revisited. Each search should have its own visited set.

        time: O(4^n) --> n is the number of characters in the board
        memory: O(n)
        """
        # Iterate through board starting searches whenever an instance of the first character in word is found
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    found = self._helper(board, word, 0, i, j, set())
                    if found:
                        return True
        return False
    
    def _helper(self, board, word, word_idx, i, j, visited):
        """
        Helper function to perform dfs within the board. Takes the coordinates of the current cell, as well as a set of visited cells and the
        word, board and the current idx in the word. Returns true if the final character in the word is found or false otherwise.
        """
        # Check if this character is in the word. Return false if not
        if board[i][j] != word[word_idx]:
            return False
        
        word_idx += 1
        # Whole word has been found
        if word_idx >= len(word):
            return True
        
        # Record this cell as visited
        visited.add((i, j))

        # If the characters match, start searches in the up, down, left and right directions
        up, down, left, right = False, False, False, False
        if i - 1 >= 0 and (i-1, j) not in visited:
            up = self._helper(board, word, word_idx, i-1, j, visited)
        if i + 1 < len(board) and (i+1, j) not in visited:
            down = self._helper(board, word, word_idx, i+1, j, visited)
        if j - 1 >= 0 and (i, j-1) not in visited:
            left = self._helper(board, word, word_idx, i, j-1, visited)
        if j + 1 < len(board[i]) and (i, j+1) not in visited:
            right = self._helper(board, word, word_idx, i, j+1, visited)
        
        # Only one path needs to find the word
        if not (up or down or left or right):
            # If this path does not find a valid solution it does not mean another path won't as well. I should remove this cell so that
            # another path can explore it
            visited.remove((i, j))
        return up or down or left or right
        
