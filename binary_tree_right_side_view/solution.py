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
            # Create q to store children of nodes popped from main q
            level_q = deque()
            # Create boolean to track if the node being popped from the main q is the first for the level
            is_first = True
            while len(q) != 0:
                node = q.popleft()
                if is_first:
                    res.append(node.val)
                    is_first = False
                # Add children of node to level q so main q can be exhausted for the level
                if node.right:
                    level_q.append(node.right)
                if node.left:
                    level_q.append(node.left)
            # Empty the level q back into the main node
            while len(level_q) != 0:
                q.append(level_q.popleft())
        return res
            
        
