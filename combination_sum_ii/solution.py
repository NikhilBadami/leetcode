class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        This problem is similar to the original combination sum problem, except instead of being able to re-use a number
        an infinite number of times, we are limited to the number of times the number appears in the candidates array.
        While iterating through, I can define my recursion tree as follows: The left sub-tree is allowed to re-use the
        current element. The right subtree cannot and must move on to the next unique value in candidates. If the left
        sub-tree exhausts the current element, it is allowed to use the next unique element it encounters. Note that to
        achieve this I will need to sort the input before processing, however, compared to the overall runtime, this is
        not a bottle neck for time efficiency.

        time: O(n * 2^n) --> Each element can only be used once and we loop during recursion to skip elements
        memory: O(2^n)
        """
        # Sort input to make it easier to detect duplicates
        candidates.sort()
        res = []
        self._helper(candidates, target, res, 0, ([], 0))
        return res
    
    def _helper(
        self,
        candidates,
        target,
        res,
        cur_idx,
        cur_soln
    ):
        """
        Helper function used to calculate solution. Takes the input from the main function, a list to track the current
        solution, the current index and a list tracking the overall solution
        """
        # Handle base cases
        cur_list, cur_sum = cur_soln
        if cur_sum == target:
            res.append(cur_list.copy())
            return
        if cur_idx >= len(candidates) or cur_sum > target:
            return
        
        # Create left sub-tree
        cur_list.append(candidates[cur_idx])
        cur_sum += candidates[cur_idx]
        self._helper(candidates, target, res, cur_idx+1, (cur_list, cur_sum))

        # Undo left operations and create right sub-tree
        cur_list.pop()
        cur_sum -= candidates[cur_idx]
        next_idx = cur_idx + 1
        while next_idx < len(candidates) and candidates[cur_idx] == candidates[next_idx]:
            next_idx += 1
        self._helper(candidates, target, res, next_idx, (cur_list, cur_sum))
        
        return


        
