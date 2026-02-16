class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        We are given an array of points and asked to find the minimum cost to connect all points. All points are considered connected if there
        is exactly one simple path between any two points. Globally, this means that the path from one point to another cannot branch of have
        multiple paths, i.e., a point cannot have a path to another point while also being connected to that point. The cost to connect two
        points is the manhattan distance between the two points.

        If I view the points as the nodes in an undirected graph, then the goal of the problem is to find the minimum spanning tree of the
        graph. The minimum spanning tree is a subset of edges that connects all points while not having any cycles and having the minimum
        edge cost.

        I can solve this using Kruskal's algorithm to find the minimum spanning tree of a graph. The algorithm works as follows:

        1: Sort edges by edge weight in ascending order. Edges can be stored as e_i = (a_i, b_i, w_i)
        2: Iterate through the edges and add the two endpoints to the same group, or union them, if they are already not in the same group.
           Otherwise, ignore this edge as adding it would introduce a cycle
        3: Continue until all edges have been processed

        This algorithm can be realized using union find, which is a dataset that defines two operations:

        Union: Given two nodes, adds them to the same set if they are not already in the same set
        Find: Finds the parent of a given node

        As a final optimzation, I can implement path compression, where every node in the same group points to the root of the overall group
        instead of the node that added it to the group. Groups will be merged such that smaller groups are merged into larger groups

        time:
          Operations:
            - Calculate weights for all edges. Edges are the connection from each point to every other point. This means for each point, I need
              to calculate the distance to every other point. If there are n points, this is O(n^2)
            - Sort the edges in ascending order based on weight (distance) which is O(elog(e))
            - Union/Find operations occur in nearly constant time
          Overall: O(e^2) --> e is the number of edges
        memory: O(e^2)
        """
        # First calculate edge weights
        edges = []
        for i in range(len(points)):
            p1 = points[i]
            for j in range(i+1, len(points)):
                p2 = points[j]
                edges.append((i, j, self._distance(p1, p2)))
        
        # Sort edges based on weight
        edges.sort(key=lambda x: x[2])

        # Iterate through edges performing union find.
        # Initially, each node's parent is itself. Parent are 0 indexed. The number of points is given by len(points)
        parents = [i for i in range(len(points))]
        # Tracks size of each group, which is initially 1
        _size = [1 for i in range(len(points))]
        min_cost = 0
        for e in edges:
            p1, p2, w = e
            if self._union(p1, p2, parents, _size):
                min_cost += w
        return min_cost
    
    def _union(self, p1, p2, parents, _size):
        """
        Given two nodes, checks to see if they are part of the same group by checking their parents. If they are, return False, meaning that this
        edge should not be considered in the final solution. If they are not part of the same group, union them based on which group is larger
        and return True, indicating that this edge should be included in the final cost calculation. Updates parents and sizes in place.
        """
        # Get parents of each node
        par1, par2 = self._find(p1, parents), self._find(p2, parents)
        if par1 == par2:
            return False
        if _size[par1] > _size[par2]:
            # Union par2 into par1
            parents[par2] = par1
            _size[par1] += _size[par2]
        else:
            # Union par1 into par2
            parents[par1] = par2
            _size[par2] += _size[par1]
        return True
    
    def _find(self, p, parents):
        """
        Given a point, attempts to find the root node. Performs path compression as well
        """
        # Base case if the node is its own parent
        if p == parents[p]:
            return p
        # Iterate up the tree starting from this node to find the root. Children point to parents
        parent = self._find(parents[p], parents)
        parents[p] = parent
        return parent
    
    def _distance(self, p1, p2):
        """
        Given two points represented as a list [x, y], calculate the manhattan distance given by abs(x_1 - x_2) + abs(y_1 - y_2)
        """
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
