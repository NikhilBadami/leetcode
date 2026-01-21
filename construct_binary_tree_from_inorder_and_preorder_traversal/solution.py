# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        I'm given two arrays, preorder and inorder, which represent the tree after processing it in using preorder and inorder traversals
        respectively. I need to reconstruct the tree using these two arrays.

        Preorder traversal processes the root first, then processes the left child and then finally the right child. Inorder traversal processes
        the left child, then the root then the right child. The first element in the preorder array will be the root of the tree. I know that in
        the inorder array, every element that appears before this node must be in the roots left subtree, and every node that appears after the
        node in the inorder array must be in the nodes right subtree. I can use this element to partition the inorder array.

        How can I identify the roots of the sub-trees, i.e., node 20? Because the preorder array processes the root before processing every
        child, I can assume that each node in the preorder array is the root of its own subtree, and partition the inorder array accordingly.
        So for the given arrays in example 1, I can partition the inorder array by 3 first, resulting in subarrays [9] for the left subtree and
        [15,20,7] for the right subtree. In the left subtree, I can move to the next element in the preorder array, which is 9. This 9 has access
        to the inorder array [9]. Since I cannot partition the inorder array anymore, I simply create a node out of the current 9 and return.

        In the right subtree, I pass 20 as the root of this subtree and have the inorder array [15,20,7] to work with. I partition this subarray
        around 20 and pass 15 from the preorder array and [15] from the inorder array to the left subtree, and 7 from the preorder array and [7]
        from the inorder array to the right subtree. Like with 9, because the inorder arrays can no longer be partitioned, I simply create nodes
        from 15 and 7 and return. For other examples, I repeat this process until the tree is fully constructed.

        time: O(n) --> I process each node at most twice, once in preorder and once in inorder
        memory: O(h) --> memory for call stack. Will use pointers to identify array slices so no additional memory is used for slice copies
        """
        # Helper global variables
        self.inorder_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        return self._helper(preorder, inorder, 0, len(inorder))
    
    def _helper(self, preorder, inorder, i, j) -> Optional[TreeNode]:
        """
        Helper method. Takes preorder and inorder arrays along with the bounds of inorder array slice. Returns the root of the current subtree
        """
        # Handle base cases
        if i >= j:
            return None

        # Create root node based on current index of preorder array
        root = TreeNode(val=preorder[self.pre_idx])
        # Increment preorder counter since this node was used
        self.pre_idx += 1
        inorder_idx = self.inorder_map[root.val]

        # Create left and right sub-trees
        root.left = self._helper(preorder, inorder, i, inorder_idx)
        root.right = self._helper(preorder, inorder, inorder_idx+1, j)
        return root

