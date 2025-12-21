# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Use BFS to iterate over the tree level by level. If I iterate over the tree from right to left, the first node
        out of the queue at each level is going to be the right most node for that level. While iterating, I should use
        a second node to store the children of the nodes being popped out of the main queue so I can ensure I am processing
        each level separately.

        time: O(n) --> n is the number of nodes in the tree
        memory: O(n)
        """
        res = []
        # Handle edge case
        if not root:
            return res
        
        from collections import deque
        q = deque()
        q.append(root)
        while len(q) != 0:
            # Get number of nodes in level
            level_size = len(q)
            for i in range(level_size):
                node = q.popleft()
                if i == 0:
                    # This is the first node in the level and therefore the right most node
                    res.append(node.val)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

        return res
            
        
