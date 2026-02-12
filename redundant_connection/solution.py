class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        I am given a graph that started as a tree, where a tree is defined as an undirected graph that is connected and has no cycles. A single
        edge has been added to this tree that breaks the tree property described earlier. I need to identify an edge that can be removed so that
        the graph is a tree again. If there are multiple possible edges, I should return the last edge that occurs in the input.

        Since this graph was a tree that was connected and had no cycles, I know that adding an additional edge must introduce a cycle somewhere
        in the graph. This means that this problem is really a cycle detection problem. Since I specifically want to identify the last edge
        in the input that could solve this problem, I can use the union find datastructure.

        Union-Find is a data structure that tracks various sets of nodes. This data structure has two key functions: union and find. The union
        operation takes two nodes and combines them into a single set. If the nodes were already part of their own larger sets, these
        two sets are joined together. The find operation is used to find the parent of a given node which could be itself, or the parent of
        the cluster it is a part of.

        This datastructure can be used to find cycles as follows: I can iterate through the edges input and union the endpoints of each edge
        together. As I iterate through, if I find an edge that contains endpoints that are already part of the same set, I know that this
        edge both introduces a cycle into the graph and can be removed and meets the requirement of the problem to return the last occurrence of
        a possible answer.

        To improve the efficiency of the problem, I can use path compression and union by rank. Path compression makes it so that each node in 
        the cluster points to the root of that cluster. For example, say nodes 1 and 2 are unioned together with 1 as the parent of the set. If
        2 and 3 are then unioned together, instead of setting 2 as the parent of 3, I set the parent of 3 to be 1, since 1 is the parent of the
        larger set.

        Union by rank means that smaller set are added to larger sets. So 3 is added to the set containing 1 and 2 since that set is larger. With
        these efficiencies added, the time complexity of the union and find operations is near constant.

        time: O(n + e)
        memory: O(n + e)
        """
        # A connected tree has exactly n-1 edges, so a tree with a single added edge has n edges and n nodes
        n = len(edges)
        # Use array to track initial parents of nodes, which is themselves. This array is 1-indexed i.e., 0 is never used
        self.parents = [i for i in range(n + 1)]
        # Track size of each cluster based on parent. Each size is 1 since each node is initially its own cluster and its own parent
        self.sizes = [1] * (n+1)
        for e in edges:
            n1, n2 = e
            if not self.union(n1, n2):
                return e

    
    def union(self, n1, n2):
        """
        A modified union operation that suits the purposes of this problem. Takes two nodes n1 and n2 and checks to see if they have the same
        parent. If they have the same parent, they are already part of the same set and adding the edge that triggered this union operation
        introduces a cycle to the graph. This function should return False and the edge that triggered this call is the answer to the problem.

        If the nodes are not part of the same set, they should be unioned together following the principles of union by rank described above
        """
        par1 = self.find(n1)
        par2 = self.find(n2)
        if par1 == par2:
            # This edge introduces a cycle because these nodes are already part of the same group
            return False
        # Union together these two nodes. The smaller set is added to the larger set
        if self.sizes[par1] > self.sizes[par2]:
            # Union set 2 into set 1
            self.parents[par2] = par1
            self.sizes[par1] += self.sizes[par2]
        else:
            self.parents[par1] = par2
            self.sizes[par2] += self.sizes[par1]
        return True
    
    def find(self, n):
        """
        Finds the parent of the given node. Also performs path compression by updating the parent of nodes to be the parent of the overall set
        during processing.
        """
        # Base case is if the parent of a node is itself. This means this is the root of the cluster
        if n == self.parents[n]:
            # Return this node as the root of the cluster
            return n
        par = self.find(self.parents[n])
        # This line performs path compression. Any node in this cluster should have the root parent as its direct parent
        self.parents[n] = par
        return par
        
