class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        I'm given a number, n, as well as a list of edges between nodes in a graph. I need to
        determine if these edges form a valid tree.

        What forms a valid tree? A valid tree has a single root. In a valid tree, every node
        is reachable from the node (i.e., there are no nodes with no children/parents unless
        the size of the tree is 1). In a valid tree, there are no "skip" connections, i.e., there
        are no nodes that connect to any nodes more than one level below them like in example 2.

        I can generally solve this problem by using breadth first search starting at the root.
        BFS will iterate over the tree level by level. If I track a visited set, I can check
        to see if I visit any nodes more than once. If there are any skip connections I will
        detect this because multiple nodes will have a particular node as a child (in a valid
        tree, each node can only have one parent, bfs catches this too).

        I can process the edges input into a graph by creating an adjacency list that hashes
        the node value to the list of nodes that are its children.

        How can I determine the root of the tree? The root of the tree is the node that has
        no parent. I can detect this node as follows. Create a set with all node values inside it.
        I then traverse the adjacency list and check to see which nodes appear in any of the
        lists. If a node appears in any other nodes list, it has a parent and cannot be the root.
        At the end of the iteration, if there is only one node, this must be the root. If there
        is more than one, the tree is not valid.

        time: O(n + e) --> n is the number of nodes and e is the number of edges
        memory: O(n + e)
        """
        # Create adjacency list out of input. Also create root set to find root
        graph = {}
        roots = set()
        for i in range(n):
            graph[i] = []
            roots.add(i)
        for e in edges:
            graph[e[0]].append(e[1])
            if e[1] in roots:
                roots.remove(e[1])

        # Detect root
        if len(roots) != 1:
            return False
        root = roots.pop()
        
        # Traverse the graph using BFS
        from collections import deque
        q = deque()
        q.append(root)
        visited = set()
        while len(q) != 0:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node in visited:
                    return False
                visited.add(node)
                children = graph[node]
                for child in children:
                    q.append(child)
        return True

