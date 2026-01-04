"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        I need to create a deep copy of the given input list, which in addition to a next pointer also contains a random pointer that
        points to any node in the list or null. One option is to have two pointers, one following the cur pointer in the original list
        and the random pointer. I would create both nodes and then move to the current nodes next pointer and the random nodes next
        random pointer. The question becomes how to maintain references to these nodes as I jump around the array.

        I could hash each original node to its new counter part. This way when if I jump to some node using the random pointer, I
        can check the map to see if this node was already copied and re-use this objects. This way, I don't lost references to any
        node.

        time: O(n)
        memory: O(n)
        """
        if not head:
            return None
        
        # Copy list. Use a dummy head to point to the new head to make iteration easier.
        cur = head
        random = None
        dummy = Node(0)
        prev = dummy
        nodes = {}
        while cur:
            # Copy the current node
            if cur not in nodes.keys():
                new_node = Node(cur.val)
                nodes[cur] = new_node
            else:
                new_node = nodes[cur]
            # If the random pointer is not none, copy it
            new_random = None
            if random:
                # Only copy if random wasn't already previously copied
                if random not in nodes.keys():
                    new_random = Node(random.val)
                    nodes[random] = new_random
                else:
                    new_random = nodes[random]
            # Set the new nodes on prev which also acts as a tracker node right behind cur
            prev.random = new_random
            prev.next = new_node
            random = cur.random
            cur = cur.next
            prev = prev.next
        # The above loop will end when cur is none meaning the final node in the new list will not have its random node set
        # Because each node should have already been copied by now, we set the node that prev currently points to random pointer
        # to the node the random pointer maps to
        if random:
            prev.random = nodes[random]
        return dummy.next
            
        
