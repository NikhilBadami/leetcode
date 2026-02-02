class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        I am given a number of courses and a list of pre-reqs and I need to determine 1: if the course schedule is doable and 2: what a valid
        ordering of those courses might look like.

        I can solve the problem as follows. First, I can convert the courses into a graph by building an adjacency list out of the prereq input.
        I can check if the course is doable by attempting to detect cycles in the graph; if any exist, the schedule is not doable.

        To help with building the course schedule, I can build the graph such that each class points to a list of its prereqs. I then traverse
        the graph until I find a class with no prereqs. If there is no cycle in this path, I can add this class to the output.

        time: O(n + p) --> n is the number of classes and p is the number of pre-reqs
        memory: O(n + p)
        """
        # Convert input into adjacency list
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for p in prerequisites:
            graph[p[0]].append(p[1])
        
        # Perform dfs to find cycles. If no cycles are found, add the classes to a result list
        res = []
        safe = set()
        for c in graph.keys():
            path = set()
            path.add(c)
            cycle = self._build_schedule(graph, c, path, safe, res)
            if cycle:
                return []
        return res
    
    def _build_schedule(self, graph, c, path, safe, res):
        """
        Takes the graph representation of the input, a current class, a set representing the current path and the result array and performs dfs
        to detect cycles in the graph. If not cycles are found, adds the classes to the result that are in the current path. Returns False if
        no cycle is found or True if one is found.
        """
        if c in safe:
            return False
        if len(graph[c]) == 0:
            # Found a class with no prerequisites
            res.append(c)
            safe.add(c)
            return False
        
        for cl in graph[c]:
            if cl in path:
                return True
            path.add(cl)
            cycle = self._build_schedule(graph, cl, path, safe, res)
            if cycle:
                return True
            path.remove(cl)
        safe.add(c)
        res.append(c)
        return False
        
