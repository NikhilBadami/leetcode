class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        I am given a network of nodes labeled 1 --> n as well as a list of times representing the amount of time it takes a signal to travel from
        node a to node b. I need to determine the minimum amount of time it would take for a signal sent from node k to reach all other nodes in
        the graph, or return -1 if this is not possible. Note that the graph is directed so the edges do not go both ways.

        I can maintain a set of unvisited nodes and remove nodes from this set as they are processed. This way, after I am done processing all
        the edges reachable from k, I will know if there are any unvisited nodes. If the set is not empty, the problem is not solved.

        To determine the minimum time I can do the following. I can use a priority queue to perform breadth first search starting from node
        k. Each entry into the queue will be a tuple of the node and its current distance from the starting node k. Nodes will be processed in
        priority of their distance from k. Because I am doing a BFS, the first time I encounter a node is guaranteed to be the first time that
        node is ever seen. I can record the minimum time for each node to be reached in a hash map. Once each node has been visited, I can
        iterate through this hash map and find the largest value

        time: O(elog(n)) --> Each node is only processed once
        memory: O(n) --> priority queue and unvisited set
        """
        # Process nodes into an unvisited set
        unvisited = {i for i in range(1, n+1)}

        # Create adjacency list from times
        graph = {}
        for i in range(1, n+1):
            graph[i] = []
        for t in times:
            graph[t[0]].append({
                'time': t[2],
                'node': t[1]
            })

        # Create priority queue
        import heapq
        pq =[]
        heapq.heapify(pq)

        # Perform bfs
        heapq.heappush(pq, (0, k))
        min_times = {i: float("inf") for i in range(1, n+1)}
        visited = set()
        while len(pq) != 0:
            # Get current size of "level"
            _size = len(pq)
            for _ in range(_size):
                time, node = heapq.heappop(pq)
                # Nodes can be visited multiple times. Only remove on first visit
                if node in unvisited:
                    unvisited.remove(node)
                visited.add(node)
                min_times[node] = min(min_times[node], time)
                for neighbor in graph[node]:
                    if neighbor['node'] not in visited:
                        heapq.heappush(pq, (time + neighbor['time'], neighbor['node']))
        
        # Check if all nodes were visited
        if len(unvisited) != 0:
            return -1
        min_time = 0
        for key in min_times.keys():
            min_time = max(min_times[key], min_time)
        return min_time
        
