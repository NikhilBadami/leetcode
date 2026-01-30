class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        I am given an int representing the number of courses I need to complete, as well as a list of pre-requisites. The prerequesities are
        listed as [a, b] where b is the prerequisite for course a. I need to determine if it is possible to take all the courses based on the
        prerequisites.

        I can convert the prerequisite list into a graph by mapping each pre-req to a list of classes that it is a pre-req for. Then I can solve
        the problem by iterating through this map and seeing if there are any cycles in the list. If there are, the schedule is impossible.
        Otherwise, the schedule is valid.

        time: O(p^2) --> p is the number of pre-reqs.
            - Imagine one long graph of pre-reqs, like a linked list. I would end up iterating this entire list once for each class
        memory: O(p + n) --> Recursion stack is only as big as the number of pre-reqs and I will have n lists of pre-reqs at most
        """
        # If there are no pre-reqs I can take all of the courses
        if len(prerequisites) == 0:
            return True
        
        # Process pre-reqs list into map
        graph = {}
        for n in range(numCourses):
            graph[n] = []
        for r in prerequisites:
            graph[r[1]].append(r[0])
        
        # Traverse the graph using dfs starting from each key
        for c in graph.keys():
            visited = set()
            visited.add(c)
            cycle = self._dfs(graph, c, visited)
            if cycle:
                return False
        return True
    
    def _dfs(self, graph, c, visited):
        """
        Traverses the graph starting at the given class. If the list of pre-reqs is empty, returns True, Tracks a visited set. If any class
        is seen more than once, returns False
        """
        if len(graph[c]) == 0:
            return False
        
        # Start search for each class this class is a pre-req for
        for cl in graph[c]:
            if cl in visited:
                return True
            visited.add(cl)
            cycle = self._dfs(graph, cl, visited)
            if cycle:
                return True
            visited.remove(cl)
        return False
        
