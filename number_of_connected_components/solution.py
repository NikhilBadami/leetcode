class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Given a number of nodes and a list of edges representing an undirected edge between two
        nodes, I need to determine the number of connected components within a graph. A
        connected component is a grouping of nodes such that you can reach all the nodes within
        the component. This grouping does not need to contain all nodes in the graph.

        I can start by converting the edges into an adjacency list. I can process each
        node into a set of unvisited nodes, and then arbitrarily pick a node to begin processing
        at. After processing one componenent, I check my unvisited set. If the set is empty,
        I have visited all the nodes and identified all components. If the set is not empty,
        there are more components to search and I must start my search again from a new node.
        Once all components have been identified, I return the number I found.

        time: O(n + e) --> n is the number of nodes and e is the number of edges
        memory: O(n + e)
        """
        # Process input into a graph
        graph = {}
        unvisited = set()
        for i in range(n):
            graph[i] = []
            unvisited.add(i)
        for e in edges:
            # Graph is undirected so the relationship exists for both nodes in an edge
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        
        # Process the graph
        num_components = 0
        while len(unvisited) > 0:
            # Pick a node in unvisited and begin a bfs to find all connected nodes
            node = unvisited.pop()
            self._bfs(node, graph, set(), unvisited)
            num_components += 1
        return num_components
    
    def _bfs(self, node, graph, visited, unvisited):
        """
        Performs a bfs starting from the given node and tries to find all connected nodes.
        Removes nodes from global unvisited set as they are encountered
        """
        from collections import deque
        q = deque()
        # Store tuples of the node to be processed as well as this nodes parent. This is
        # necessary to avoid false positive loop detections i.e., avoid adding a parent
        # multiple times
        q.append((node, None))
        while len(q) != 0:
            size = len(q)
            for _ in range(size):
                n, prev = q.popleft()
                visited.add(n)
                if n in unvisited:
                    unvisited.remove(n)
                for neighbor in graph[n]:
                    if neighbor not in visited and neighbor != prev:
                        q.append((neighbor, n))
        
