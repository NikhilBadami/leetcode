# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Brute force solution is keep a set of every encountered node and return True is a duplicate is found i.e., a node
        is revisited

        time: O(n)
        memory: O(n)

        A better way would be to use a fast and slow pointer. If one pointer is moving every two nodes and another pointer
        is moving only one node at a time, it is guaranteed that they will point to the same node at some point if there
        is a cycle.

        time: O(n)
        memory: O(1)
        """
        # Handle edge case
        if not head:
            return False
        
        slow = head
        fast = head.next
        while fast and fast.next:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
        
