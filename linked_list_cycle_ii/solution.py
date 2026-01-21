# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Can use Floyd's algorithm to both determine if a cycle exists and what the start of this cycle is. The algorithm begins by starting a
        slow and fast pointer at the head of the list. If one of the pointers reaches null at any point, there is no cycle. Otherwise, there is a
        cycle and the two nodes are guaranteed to meet. I can then restart the fast pointer from the head, this time moving only one node at a
        time, and move the slow pointer simultaneously from the meeting point and the two nodes are guaranteed to meet at the start of the cycle.
        This is because the distance from the meeting point to the head of the cycle and the distance from the head of the linked list to the head
        of the cycle are the same. Proof:

        Say l represents the distance from the head of the linked list to the head of the cycle
            x represents the distance from the head of the cycle to the meeting point of the two nodes
            c represents the total length of the cycle
        
        The distance travelled by the slow pointer is given by l + Sc + x, where S is the number of times the slow pointer fully traverses the
        cycle before it meets with the fast pointer. The distance of the fast pointer is given by l + Fc + x, where F is analagous to S. Since the
        fast pointer is travelling twice as fast as the flow pointer, I know that d_s = 2d_f or
        2(l + Sc + x) = l + Fc + x
        2l + 2Sc + 2x = l + Fc + x
        l + x = Fc - 2Sc
        l + x = c(F-2S)

        F - 2S is the total number of times the cycle is traversed, however, because it is a constant, we can ignore it for the purposes of this
        proof

        l + x = c
        l = c - x

        c - x represents the distance from the meeting point back to the head of the cycle, which is equivalent to the distance from the head of
        the linked list to the head of the cycle.

        time: O(n)
        memory: O(1)
        """
        if not head or not head.next:
            return None

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if not fast or not fast.next:
                # No cycle found
                return None
            if fast == slow:
                break

        # Reset the fast pointer and iterate until slow and fast meet again
        fast = head
        while True:
            if fast == slow:
                return fast
            fast = fast.next
            slow = slow.next
        return None

