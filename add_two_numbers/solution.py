# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        I need to add two non-negative integers represented as linked lists. The lists are given in reverse order, meaning the number 123 would
        be given as 3->2->1, so the ones digit is the first digit I encounter. I can follow a standard addition algorithm for this. I begin
        at the ones position and add the two numbers together. If their sum exceeds 10, I take a carry bit as sum // 10. The digit I keep for
        the final sum is given by sum % 10. For example, 19 + 9 = 28. I get the first digit by doing (9+9) = 18 % 10 = 8, and the carry is
        18 // 10 = 1. I need to consider if one of the lists is a longer than the other. In the case that one of the lists is exhausted, I
        continue adding the digits from the remaining list along with the carry bit until that list is exhausted (i..e, assume the rest of the
        exhausted list is 0).
        
        time: O(n+m) -> n and m are the sizes of the two input lists
        memory: O(s) -> s is the size of the list representing the sum
        """
        # Create a dummy head to make it easier to start building the result list
        dummy = ListNode()
        
        # Initialize variables used to build result
        carry = 0
        cur1 = l1
        cur2 = l2
        cur_res = dummy
        while cur1 and cur2:
            # Add these two digits along with any carry
            val1 = cur1.val
            val2 = cur2.val
            s = val1 + val2 + carry
            # Set new node and carry
            carry = s // 10
            new_node = ListNode(val=s % 10)
            cur_res.next = new_node
            cur1 = cur1.next
            cur2 = cur2.next
            cur_res = cur_res.next
        
        # Check to see if one of the pointers is still active
        cur = None
        if cur1 and not cur2:
            cur = cur1
        elif cur2 and not cur1:
            cur = cur2
        while cur:
            s = cur.val + carry
            carry = s // 10
            new_node = ListNode(val=s % 10)
            cur_res.next = new_node
            cur_res = cur_res.next
            cur = cur.next
        if carry != 0:
            cur_res.next = ListNode(val=carry)
        return dummy.next

