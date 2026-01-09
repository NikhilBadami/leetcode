# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        I need to find the kth smallest element in a binary search trees. Binary search trees have the property where for each root, every element
        in the left sub-tree must be less than the root and every element in the right sub-tree must be greater than the root. Each sub-tree
        must also themselves be a bst.

        One naive approach could be to simply go left to find the smallest element, but this can fail to actually find the smallest element. For
        example, consider the tree with root 5, left sub-child 1 which has a right sub-child of 4 and which has subsequent children of 3 and 2.
        This is a valid bst, but simply going left would fail to find the smallest element of 1.

        Another approach could be to pass a max-heap of size k that tracks the k smallest elements encountered so far. The top of the heap will
        be the kth smallest element. For example, say I have a tree with the nodes [4,3,2,1] and I want to find the 3rd smallest element. Assume
        I process 1 last. This means by the time I reach one, the heap will have element 2,3 and 4 in it, with 4 being the top of the stack. I can
        insert 1 into the heap and then pop off the largest element (4) which will leave 3 at the top of the heap, which is the 3rd smallest
        element.

        time: O(n + nlog(k)) --> I need to visit potentially every node in the tree and proces the heap potentiall every node of the tree
        memory: O(h + k) --> Memory needed the the height of the tree (i.e., the depth of the recursive stack) and the size of the heap
        """
        # Initialize the heap
        import heapq
        heap = []
        heapq.heapify(heap)
        # Run the recursive search, which updates the heap in place
        self._helper(root, k, heap)
        # Return the top of the heap, which is the kth smallest element in the tree
        # Note that the elements have been negated to make the heap a max heap
        return -heapq.heappop(heap)

    def _helper(self, node, k, heap):
        """
        Helper method to perform search. Takes the current node, k and the heap. Returns nothing --> the heap is modified in place
        """
        # Handle base cases
        if not node:
            return
        
        # Process the current node. Note the value needs to be negated to turn this into a max heap
        heapq.heappush(heap, -node.val)
        # If the heap size exceeds k, pop the top of the heap, which is the largest element
        if len(heap) > k:
            heapq.heappop(heap)
        
        self._helper(node.left, k, heap)
        self._helper(node.right, k, heap)

        return

