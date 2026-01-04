# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        I need to validate if the tree given to me constitutes a valid binary search tree. A binary search tree is valid if every
        child in its left subtree is strictly less than the given node and every value in its right subtree is strictly greater than
        the given node. Additionally, each individual subtree must form a valid BST.

        I can solve this by passing in a range. Starting at the root, the range of possible value is [-inf,inf]. However, as I
        process the tree, this range shrinks based on the node values. For example, from the root, going left limits the
        maximum value any node in the left sub tree can take. In the first given example, the range of possible values for
        the first left child is [-inf,2]. Similarly, the first right child in the first example must fall in the range [2,inf].
        In other words, when going left, update the upper bound as min(upper_bound, node.val) and when going right update the
        lower bound as max(lower_bound, node.val)

        time: O(n)
        memory: O(h)
        """
        return self._helper(root, float("-inf"), float("inf"))
    
    def _helper(self, node, lower, upper):
        """
        Helper function takes current node and current lower and upper bounds. Returns True if the node falls within the bounds and
        False if not
        """
        if not node:
            return True
        
        valid = node.val > lower and node.val < upper
        if not valid:
            return False
        return self._helper(node.left, lower, min(upper, node.val)) and self._helper(node.right, max(lower, node.val), upper)
        
