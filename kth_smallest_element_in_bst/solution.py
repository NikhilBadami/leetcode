# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        I'm given a bst and a value k and am being asked to find the kth smallest element in the binary search tree. A binary search tree is a
        tree such that every element in a nodes left sub-tree is less than the node and every element in the right sub-tree is greater than the
        node.

        If we process this tree in-order, i.e., left->node->right, we would get the tree in sorted order. This means that I can track how many
        nodes have been processed and simply return the kth node that is processed.

        time: O(n)
        memory: O(h)
        """
        val, _ = self._helper(root, k, 0)
        return val
    
    def _helper(self, node, k, count):
        """
        Helper method takes current node, k as well as how many nodes have been processed so far. Returns the current smallest val and the current
        count
        """
        if not node:
            # return -1 as a default value since all the nodes in the tree are guaranteed to be greater than or equal to 0
            return -1, count
        
        val, count = self._helper(node.left, k, count)
        if val != -1:
            # The smallest element has been found already
            return val, count

        count += 1
        if count == k:
            return node.val, count

        return self._helper(node.right, k, count)
        
