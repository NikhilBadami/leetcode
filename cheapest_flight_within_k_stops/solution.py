class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        I am given a list of flights that represents flight routes between n cities along with the price to take that flight. Given a source,
        destination and stop limit (k), I need to determine the cheapest flight. For example, if k = 1, I need to find the cheapest flight
        from src to dst with at most 1 stop. Note that if a cheapter flight exists with 0 stops, then this flight is the correct answer.

        To solve this I could use a weighted depth first search, in other words, follow the cheapest path as long as I am within my stop budget.
        If the budget is exceeded, immediately stop searching and return. Using a weighted DFS guarantees that I explore cheaper routes
        fully before exploring more expensive routes. I continue searching until I either find the destination, or I run out of options to
        search, in which case I return -1.

        From an implementation perspective, I can use a priority queue to store neighbors of each node and pop them off the queue as I iterate.
        The graph itself can be represented as an adjacency list.

        I can further optimize this by tracking nodes that have been visited before and checking their status. If they have been found to lead
        to the dst, I hash the cost from this node to reach the destination.

        time: O(elog(e)) --> complexity dominated by iterating priority queue
        memory: O(e)
        """
        import heapq
        # Create graph
        graph = {}
        for i in range(n):
            graph[i] = []
        for f in flights:
            # Heap stores tuples of (price, destination)
            heapq.heappush(graph[f[0]], (f[2], f[1]))
        
        # Search starting from src
        # Cache to track node costs to avoid repeated work
        visited = {}
        return self._dfs(graph, src, dst, k, 0, visited)
    
    def _dfs(self, graph, cur, dst, k_rem, cur_cost, visited):
        """
        Helper function to perform dfs from the current node, cur. Takes the overall destination and the number of stops remaining. Exhausts
        all paths from the current node in an attempt to reach the destination within k stops. If a valid path is found, the cost of this path
        is returned up the recursion tree. If no valid path is found, -1 is returned. All possible paths are searched to ensure the minimum cost
        is the final return value
        """
        # Base cases
        if cur == dst:
            return cur_cost
        elif k_rem == -1:
            return -1
        
        if cur in visited.keys():
            return visited[cur]
        
        # Iterate through neighbors of cur node based on price weight
        min_cost = float("inf")
        while len(graph[cur]) != 0:
            price, _next = heapq.heappop(graph[cur])
            found_cost = self._dfs(graph, _next, dst, k_rem-1, price, visited)
            if found_cost != -1:
                min_cost = min(min_cost, found_cost)
        total_price = min_cost + cur_cost if min_cost != float("inf") else -1
        visited[cur] = total_price
        return total_price
        
