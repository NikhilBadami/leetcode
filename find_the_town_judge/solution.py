class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        One way to solve this problem would be to envision the connections between townsfolk as 
        a graph. If there exists a single node such that it can be reached if iteration were
        started from any node in the graph, then this node must be the judge because it meets
        both conditions:

        1: The judge trusts no one (i.e., there are no out-going graph connections)
        2: Everyone trusts the judge (i.e., the judge can be reached starting anywhere in the
        graph)

        Failure conditions:

        1: There is no judge (i.e., there is a cycle)
        2: There are multiple candidates, i.e., there are multiple nodes with no outgoing connections

        time: O(n^2) --> Need to process potentially every node in the graph when starting at
        any node (i.e., if every node in the graph except the judge is connected to every other
        node)

        memory: O(n): Need to store a hashmap of each person in the town and how they connect to
        their trust relationships
        """
        # First, create a map with an entry for every person in the town. This map will hash
        # each person to a list of people they trust
        trust_map = {p: [] for p in range(1, n+1)}
        for relationship in trust:
            person_a = relationship[0]
            person_b = relationship[1]
            trust_map[person_a].append(person_b)

        # Iterate through the trust map. For each person, start a depth first search to see
        # if a node can be reached that has no outgoing connections. If it can, this node is
        # a judge candidate. If there is no such node, i.e., there is a cycle, return -1
        judge_candidates = set()
        for i in range(1, n+1):
            # Start a depth first search from this node
            visited = set()
            candidate = self.dfs(i, trust_map, visited)
            if candidate == -1:
                # A cycle was found so there is no point in checking the rest of the people
                return -1
            judge_candidates.add(candidate)
        
        # If there is exactly one judge candidate, then this person must be the judge. Otherwise,
        # the judge cannot be determined
        if len(judge_candidates) == 1:
            judge = judge_candidates.pop()
            # Check to see that this judge truly is in every trust array
            for p in trust_map:
                if p == judge:
                    continue
                elif judge not in trust_map[p]:
                    return -1
            return judge
        else:
            return -1
    
    def dfs(self, cur_person: int, trust_map: Dict[int, List[int]], visited: Set[int]) -> int:
        """
        Helper function to conduct a depth first search. Takes a pointer to the current person
        as well as the overall trust map. Additonally takes a visited set to protect against
        cycles. Returns the int marking the judge candidate if one is found, or -1 otherwise
        """
        # Check to see if the current node is a judge candidate
        if len(trust_map[cur_person]) == 0:
            # This person trusts no one and is a judge candidate
            return cur_person
        
        # Mark this node as visited
        visited.add(cur_person)

        # Continue dfs
        # Check to see if there are any trusted people not already visited
        for p in trust_map[cur_person]:
            if p not in visited:
                candidate = self.dfs(p, trust_map, visited)
                # If a valid candidate is found, return the candidate
                if candidate != -1:
                    return candidate

        # If no valid candidate was found, or all the nodes have been visited, return -1
        return -1
