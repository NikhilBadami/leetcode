# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        One solution is to iterate the list and read each node into a stack, then unload the stack setting the current
        pointers next to the top of the stack

        time: O(n)
        memory: O(n)

        One other way is to have two pointers and a temp variable. p1 points at the current node, p2 points to p1.next and
        temp holds p2.next. p2.next is updated to point as p1, p1 is set to p2 and p2 is set to temp. Continue until the
        entire list is reveresed.

        time: O(n)
        memory: O(1)
        """
        # Handle edge case if head is null
        if not head:
            return head
        
        p1 = None
        p2 = head
        while p2 is not None:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp
        return p1
        
