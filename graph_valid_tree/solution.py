class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        I'm given a number, n, as well as a list of edges between nodes in a graph. I need to
        determine if these edges form a valid tree.

        What forms a valid tree? A valid tree with n nodes has n-1 edges and no cycles. I can
        determine if the graph is valid by checking that the number of edges is n-1, and that
        there are no cycles in the tree.

        time: O(n + e)
        memory: O(n + e)
        """
        # If there is an invalid number of edges, return False
        if len(edges) != n - 1:
            return False
        
        # Process the edges into an adjacency list
        graph = {}
        for i in range(n):
            graph[i] = []
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        
        # Perform BFS to detect a cycle
        from collections import deque
        q = deque()
        # Since there is a valid number of edges, I'd be able to reach every node in the graph
        # starting from any other node. This is because each edge is undirected. For simplicity,
        # start at 0. Additionally, since each edge is undirected, to avoid processing the node
        # we just came from, each entry will have a prev entry to avoid false positives in
        # cycle detections
        q.append((0, None))
        visited = set()
        while len(q) != 0:
            size = len(q)
            for _ in range(size):
                node, prev = q.popleft()
                if node in visited:
                    return False
                visited.add(node)
                for child in graph[node]:
                    if child != prev:
                        q.append((child, node))

        # If the tree is valid, I should have visited every node
        if len(visited) != n:
            return False
        return True

