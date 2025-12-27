class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Ask is to return a list containing all subsets of the input list nums. A subset is a potentially non-contiguous
        set of elements within nums, including the empty set. This can be created by iterating through the nums array.
        At each element, I can choose to include the current element or not include it. This naturally creates a branching
        structure that forms a tree, which can then be iterated over to create all of the subsets. The base case is the
        empty set. From there, we follow the algorithm described above and build all possible sets. This approach
        does not create duplicates. Both DFS and BFS could be used, but for simplicity in implementation, use BFS

        time: O(2^n)
        memory: O(2^n)
        """
        from collections import deque
        q = deque()
        q.append([])
        i = 0
        while i < len(nums):
            # Get number of sets currently in q
            num_sets = len(q)
            for _ in range(num_sets):
                # Pop each set off of the q. Either include the element currently at i, or don't include it. Add both
                # sets back to the q
                s = q.popleft()
                new_s = s.copy()
                new_s.append(nums[i])
                q.append(s)  # Didn't include nums[i]
                q.append(new_s)  # Included nums[i]
            i += 1
        
        # At the end of the iteration, the q contains all possible sub-sets of nums
        return list(q)
        
