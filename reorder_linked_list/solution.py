# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        I can pre-process the list into an array, which would give me an index for each node in the list. Then, I know that
        I need to re-order the list such that the first node points to the last node, the second node to the second to
        last node etc.

        time: O(n)
        memory: O(n)
        """
        arr = []
        # Preprocess list into array giving each node an index
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        
        # Re-order list
        cur = head
        for i in range(len(arr)):
            # Need to check it iteration is done
            # If the length of the list is even, the final node to process is len(arr) / 2 - 1, which need to point to null
            if i == (len(arr) / 2) - 1:
                cur.next.next = None
                break
            # If the list is odd, the final node to process is len(arr) // 2
            if i == len(arr) // 2:
                cur.next = None
                break
            # Save existing connection
            tmp = cur.next
            cur.next = arr[len(arr) - i - 1]
            cur.next.next = tmp
            cur = tmp
        
