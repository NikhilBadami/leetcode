# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        I need to find the number of "good" nodes in the tree where a "good" node is defined as a node where there are no
        nodes with a value greater than the current nodes value. I can accomplish this by conducting a modified DFS where
        I pass a parameter tracking the largest number seen so far in the DFS. Any value that is less than or equal to
        this number is a "good" node. Additionally, I will track the solution which counts the number of good nodes seen
        so far.

        time: O(n)
        memory: O(h)
        """
        return self._helper(root, root.val)
    
    def _helper(self, node, cur_max):
        """
        Helper function that tracks the current maximum value seen so far. Returns the number of good nodes seen
        """
        # Handle base cases
        if not node:
            return 0

        cur_max = max(node.val, cur_max)
        
        # Get number of good nodes in left and right sub trees
        good_left = self._helper(node.left, cur_max)
        good_right = self._helper(node.right, cur_max)
        num_good = good_left + good_right

        # Check to see if the current node is a good node
        if node.val >= cur_max:
            num_good += 1
        
        return num_good
        
