"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        I need to make a deep copy of the given graph. I can start at the given node and create a copy of this node. I then look at
        its neighbors. I need to check if these neighbors have been copied yet or not. I can track which nodes have been copied by
        hasing their value to their new node. I also track a visited set to track which nodes have been fully copied. When creating
        the neighbors list for any given node, I either create the neighbors if they don't exist, or I pull them from the dictionary
        if they have already been created. I need to perform this check even before creating new nodes to avoid creating duplicate
        copies.

        time: O(n)
        memory: O(n) --> Need to track which nodes I've visited and which nodes have been copied. Note that these structures are
                         slightly different in purpose. The former tracks which nodes have been fully processed and the later only
                         tracks which nodes have been created
        """
        # Handle edge case of null node
        if not node:
            return None
        
        # I can use a BFS to process all nodes
        from collections import deque
        q = deque()
        q.append(node)
        # Create a dummy head whose only neighbor will be the new head
        dummy = Node()
        created = {}
        visited = set()
        while len(q) != 0:
            cur_node = q.popleft()
            if cur_node in visited:
                # Skip previously processed nodes
                continue
            # Copy the current node. First check that it wasn't previously created
            if cur_node.val not in created.keys():
                new_node = Node(cur_node.val)
                created[cur_node.val] = new_node
            else:
                new_node = created[cur_node.val]
            # Copy the current nodes neighbors list, creating new nodes as necessary
            for n in cur_node.neighbors:
                if n.val not in created.keys():
                    new_neighbor = Node(n.val)
                    created[n.val] = new_neighbor
                else:
                    new_neighbor = created[n.val]
                new_node.neighbors.append(new_neighbor)
                # Add the current neighbor to the queue based on the original node
                q.append(n)
            # Mark the current node as visited
            visited.add(cur_node)
            # If the current node is the first node, add it to the dummy's adjacency list
            if cur_node.val == 1:
                dummy.neighbors.append(new_node)

        return dummy.neighbors[0]

