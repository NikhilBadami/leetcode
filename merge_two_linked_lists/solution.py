# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Can have running pointer for both lists. On each iteration, the pointer pointing to the node with the lesser value
        is added to the new list. In the case of ties, favor list1. Have a 3rd pointer keeping track of the new list.

        Need to handle cases where one list is shorter/longer than the other. If one pointer is exhausted but the other
        isn't, simply set new_list.next = non_exhausted_pointer.next

        time: O(n) --> n is the length of the shorter list
        memory: O(1) --> list is built in place i.e., no new nodes are allocated except for dummy
        """
        # Handle edge cases
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Create dummy head for new list to handle edge caeses of figuring out which node from which list should be first
        dummy_head = ListNode()

        # Initialize pointers
        p1 = list1
        p2 = list2
        n = dummy_head
        while p1 and p2:
            if p1.val <= p2.val:
                n.next = p1
                p1 = p1.next
            else:
                n.next = p2
                p2 = p2.next
            n = n.next
        if not p1 and p2:
            n.next = p2
        elif not p2 and p1:
            n.next = p1
        return dummy_head.next
        
