class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        I'm given a number of courses and a set of prerequisites and I need to determine whether it is possible to take all of the classes based
        on the pre-reqs.

        I can solve this problem by converting the list of prereqs into an adjacency list, where each key in the graph is a prereq and its
        value is a list of classes it is a prereq for. I can then traverse this list and search for any cycles. If there are any cycles,
        the course schedule is not doable. If no cycles exist, the course schedule can be completed.

        While processing the graph, I need to keep track of which nodes have already been verified to be completable. I can do this by tracking
        a global visited, or "safe," set and a set tracking the current path of the search. The global safe set will allow us to avoid checking
        nodes more than once and the path set will help us determine if a cycle exists on the current search.

        time: O(n + p) --> n courses and p prereas
        memory: O(n + p)
        """
        # Process pre-reqs into adjacency list
        graph = {}
        for n in range(numCourses):
            graph[n] = []
        for p in prerequisites:
            graph[p[1]].append(p[0])
        
        # Process each key in the graph
        safe = set()
        for c in graph:
            cycle = self._detect_cycle(graph, c, set(), safe)
            if cycle:
                return False
        return True
    
    def _detect_cycle(self, graph, cl, path, safe) -> bool:
        """
        Helper function used to find cycles using dfs. Takes the graph representation of the prereqs, the current class, the current path
        and a global set tracking nodes that have already been verified to be completable. Returns true if a cycle is detected and false if no
        cycle is detected
        """
        # Base case adjacency list for this class is empty meaning this path is valid
        if len(graph[cl]) == 0:
            # No cycle found
            return False
        if cl in safe:
            return False
        
        for c in graph[cl]:
            if c in path:
                return True
            if c not in safe:
                path.add(c)
                cycle = self._detect_cycle(graph, c, path, safe)
                if not cycle:
                    safe.add(c)
                    path.remove(c)
                else:
                    return True
        return False
        
