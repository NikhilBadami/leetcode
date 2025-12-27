class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        The ask is to find all unique combinations that sum to target. Because the combinations need to be unique,
        permutations of existing solutions are invalid.

        The key is determining how to include elements of the candidates array in a potential solution, especially since
        elements can be re-used. Since the decision making of choosing vs. not choosing an element naturally creates
        a tree, I can define each left/right sub-tree to satisfy some condition. In this case, the left sub-tree will
        re-use the element at the current index and the right sub-tree will always increment the index.

        The time complexity can be derived as follows: For each element in the candidates array, we can make two choices.
        The deepest we can go for any given candidate c is based on how many times c can divide target, so target/c. This
        means that in the worst case, the maximum number of splits for a given c is t/c, so a big-O of 2^(t/c), which is
        also the memory complexity

        time: O(2^(t/c))
        memory: O(t/c)
        """
        return self._helper(candidates, target, 0, ([], 0))
    
    def _helper(self, candidates, target, cur_idx, cur_soln) -> List[List[int]]:
        """
        Helper method to calculate solution. Takes candidates, target and current index as input. Additionally takes
        cur_soln, which is a tuple of the current solution for this node along with the sum of that solution.
        Returns a list of solutions found from this node
        """
        # Base cases
        cur_list, cur_sum = cur_soln
        # Base case is empty list of 1D
        base_soln = []
        if cur_idx >= len(candidates) or cur_sum > target:
            return base_soln
        if cur_sum == target:
            return [cur_list]
        
        # Build tree
        # Left sub-tree re-uses the current element
        left_list = cur_list.copy()
        left_list.append(candidates[cur_idx])
        left_res = self._helper(candidates, target, cur_idx, (left_list, cur_sum + candidates[cur_idx]))

        # Right sub-tree increments the index
        right_list = cur_list.copy()
        right_res = self._helper(candidates, target, cur_idx+1, (right_list, cur_sum))

        # Build solution for this node
        if len(left_res) == 0 and len(right_res) != 0:
            return right_res
        elif len(left_res) != 0 and len(right_res) == 0:
            return left_res
        elif len(left_res) != 0 and len(right_res) != 0:
            return left_res + right_res
        else:
            return base_soln
        
