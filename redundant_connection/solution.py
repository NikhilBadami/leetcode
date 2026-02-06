class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        I am given an undirected graph represented as a list of edges. Within the context of this problem, a tree is an undirected graph that has
        no cycles. I need to determine one edge to remove from the input graph to make it a valid tree.

        I can do this by first identifying the portion of the graph that is a cycle. For example, as I am searching, if I encounter a node that
        I have already visited, then I know that this node and the other end the edge that put this node in my search queue are a valid edge
        to be removed. Note that edges are represented as [a_i, b_i] such that a_i < b_i.

        I will need to convert the edges list into an adjacency list for efficient processing. Nodes are 1-indexed. I can find the
        largest value in the graph by iterating through edges and checking the second value of the edge (since the second value is always
        larger).

        time: O(n + e)
        memory: O(n + e)
        """
        # Find largest value in graph
        n = 0
        for e in edges:
            n = max(n, e[1])
        
        # Build adjacency list
        graph = {}
        for i in range(1, n+1):
            graph[i] = []
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        
        # Search graph for cycles. When a cycle is found, remove the edge that led to the cycle detection
        from collections import deque
        q = deque()
        visited = set()
        # Since the graph id guaranteed to be connected, I can pick any node to start from
        q.append((1, None))
        while len(q) > 0:
            size = len(q)
            for _ in range(size):
                node, prev = q.popleft()
                if node in visited:
                    # Found a valid edge to remove
                    return [
                        min(node, prev),
                        max(node, prev)
                    ]
                visited.add(node)
                for neighbor in graph[node]:
                    q.append((neighbor, node))

        # Default case that should never be reached
        return []
        
